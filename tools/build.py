# Builds data/responses.json from prompt.txt (the exercise) + runs.json (who ran it) + the raw answer files.
#   python tools/build.py
import json, os, re

ROOT = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
P = lambda *a: os.path.join(ROOT, *a)

# --- the exercise: prompts and every option, straight from prompt.txt
text = open(P("prompt.txt"), encoding="utf-8").read()
prompts = []
for block in re.split(r"(?m)^### Prompt ", text)[1:]:
    num, rest = block.split(":", 1)
    question = rest.strip().splitlines()[0].strip()
    note = re.search(r"\*\(Note: (.*?)\)\*", rest, re.S)
    options = [{"letter": m[1], "text": m[2].strip()} for m in re.finditer(r"(?m)^- ([A-F]) — (.+)$", rest)]
    prompts.append({"n": int(num), "question": question, "note": note[1].strip() if note else "", "options": options})

FIELDS = {"choice": r"Choice", "reason": r"Reason", "first_step": r"First step", "blind_spot": r"Risk\s*/\s*blind spot",
          "rewrite": r"Optional rewrite"}


def parse(raw):
    raw = raw.replace("\r", "")
    heads = list(re.finditer(r"(?m)^\s*(?:#+\s*|\*\*)\s*Prompt\s+(\d)\b.*$", raw))
    preface = raw[:heads[0].start()].strip() if heads else ""
    out = {}
    for i, h in enumerate(heads):
        body = raw[h.end(): heads[i + 1].start() if i + 1 < len(heads) else len(raw)]
        ans = {}
        for key, lab in FIELDS.items():
            m = re.search(r"\*\*" + lab + r":?\*\*:?\s*(.*?)(?=\n\s*\d+\.\s*\*\*|\n\s*-{3,}|\n#|\Z)", body, re.S | re.I)
            v = re.sub(r"\s+", " ", m[1]).strip() if m else ""
            v = re.sub(r"^- You can pick more than one.*$", "", v).strip()
            ans[key] = v
        c = ans["choice"]
        m = re.match(r"^([A-F](?:\s*(?:,|and|&|/|\+)\s*[A-F])*)\b", c)
        ans["letters"] = re.findall(r"[A-F]", m[1]) if m else []
        out[int(h.group(1))] = ans
    return preface, out


runs = json.load(open(P("runs.json"), encoding="utf-8"))["runs"]
for r in runs:
    preface, answers = parse(open(P(r["file"]), encoding="utf-8").read())
    r["preface"] = preface
    r["answers"] = [dict(prompt=n, **answers.get(n, {})) for n in range(1, len(prompts) + 1)]
    missing = [a["prompt"] for a in r["answers"] if not a.get("letters")]
    if missing:
        print(f"WARNING {r['id']}: no choice parsed for prompts {missing}")

os.makedirs(P("data"), exist_ok=True)
json.dump({"exercise": {"name": "Perspective / Framing Exercise v3.1", "by": "Jaron K. Bragg",
                        "source": "https://github.com/JaronKBragg7337/Perspective-Environmental-framework-Exercise",
                        "prompts": prompts}, "runs": runs},
          open(P("data", "responses.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
for r in runs:
    print(f"{r['ai']:26} " + " ".join(f"{a['prompt']}:{'+'.join(a['letters']) or '?'}" for a in r["answers"]))
