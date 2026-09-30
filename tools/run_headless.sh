#!/bin/bash
# Framing exercise v3.1, cold (no framework, no author answers). Each AI gets prompt.txt only, from an empty folder.
C=/c/Users/lilli/AppData/Local/Temp/claude/fl-clean
O=/c/Users/lilli/AI-Shared/projects/framing-lens-2026-09
cd "$C"
( codex exec -m gpt-6-luna -c model_reasoning_effort=high -s read-only --skip-git-repo-check -C "$C" - < prompt.txt > "$O/raw-codex-gpt6-luna.md" 2>"$O/err-codex-luna.txt"; echo "luna $?" ) &
( codex exec -m gpt-6.1-sol -c model_reasoning_effort=high -s read-only --skip-git-repo-check -C "$C" - < prompt.txt > "$O/raw-codex-gpt6.1-sol.md" 2>"$O/err-codex-sol.txt"; echo "sol $?" ) &
( grok --prompt-file prompt.txt --always-approve --max-turns 4 --no-memory --no-subagents --no-plan --cwd "$C" > "$O/raw-grok-build.md" 2>"$O/err-grok.txt"; echo "grok $?" ) &
( python - > "$O/raw-deepseek.md" 2>"$O/err-deepseek.txt" <<'PY'
import json, os, urllib.request
key = next(l.split("=",1)[1].strip().strip('"') for l in open(os.path.expanduser("~/.secrets/keys.env"), encoding="utf-8") if l.startswith("DEEPSEEK_API_KEY"))
p = open("prompt.txt", encoding="utf-8").read()
for model in ("deepseek-chat", "deepseek-reasoner"):
    body = {"model": model, "messages": [{"role": "user", "content": p}]}
    req = urllib.request.Request("https://api.deepseek.com/chat/completions", data=json.dumps(body).encode(), method="POST",
                                 headers={"Content-Type": "application/json", "Authorization": "Bearer " + key})
    r = json.load(urllib.request.urlopen(req, timeout=300))
    print(f"\n\n# DeepSeek - {r.get('model', model)}\n"); print(r["choices"][0]["message"]["content"])
PY
echo "deepseek $?" ) &
( python /c/Users/lilli/AI-Shared/tools/qwen-bridge.py "$(cat prompt.txt)" > "$O/raw-qwen-local.md" 2>"$O/err-qwen.txt"; echo "qwen $?" ) &
wait
ls -la "$O"
