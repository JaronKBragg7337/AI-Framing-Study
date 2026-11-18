# Jaron's AI Tests (started as the AI Framing Study)

**See it:** https://jaronkbragg7337.github.io/AI-Framing-Study/

Jaron K. Bragg's tests for AI models, every model he can reach, every answer kept. Data, not debate: no answer is "right",
the attempt is the data. Five tests, five kinds of thinking:

- **Framing Lens:** six "what did X say to Y" prompts. Temperament: one side, both sides, "depends on perspective".
- **The wood question:** "What's the rarest material in the cosmos?" Does it follow the chain of conditions or grab the textbook answer?
- **Live-Reference Principle:** does it check its own claims against today's world?
- **The music one (instrumental version):** two coworkers, same truck, same song; one hears only the instrumental. Body or machine?
- **The picture test:** a city at night whose lit windows hide a sentence in binary. Can it find hidden structure?

Repeat runs: each model gets each test several times in fresh chats (empty folder, no memory), because one answer is one sample.
Models so far: Claude (Opus 5.5, Sonnet 5.5, Fable 5.1, Fable 5.2, Haiku 4.5/5.5), OpenAI (GPT-6 Luna, Sol 6.1, GPT-6.2 Sol, GPT-6.2 Astra, Terra 6.1 soon),
Grok Build 4.7, DeepSeek (chat, V4 Pro), Kimi, Qwen (local), plus ChatGPT runs with and without the author's memory.

`index.html` is the full notebook (built in the author's AI-Shared workspace by tools/tests-page.py, published by tools/publish_tests.py).
Every prompt, table and raw answer it is built from is in [`data/framing-lens/`](data/framing-lens) and [`data/picture-test/`](data/picture-test).
The first framing study page (Sept 2026) is [`framing-study-2026-09.html`](framing-study-2026-09.html); its original notes follow.

CC0: use any of it.

---

## The first framing study (Sept 2026)

Every AI model, given the same short exercise cold: Jaron K. Bragg's
[Perspective / Framing Exercise (v3.1)](https://github.com/JaronKBragg7337/Perspective-Environmental-framework-Exercise).
Six ambiguous prompts ("What did the bottom of the pan say to the false bottom?") with lettered options. Each AI picks,
gives a reason, a first step, its own blind spot, and an optional rewrite.

The page shows each question with **every option, who picked it, and which options no AI picked**, and each AI's full set
of answers. New models get added as they come out.

## How it's run

- Each AI gets only [`prompt.txt`](prompt.txt): the six prompts and the answer format. Not the framework, not the book,
  not the author's own answers, not earlier results.
- OpenAI models through the Codex CLI and Grok through the Grok Build CLI, each from an empty folder with memory off;
  DeepSeek through its API; Claude models as fresh Claude Code subagents with tools off. Details and caveats per run are in
  [`runs.json`](runs.json).
- **Known caveat:** the Claude subagents start inside the author's own project, so they also read its instruction file.
  Their Prompt 2 (guardrail) answers show it. Noted on each run.

## Layout

```
prompt.txt              exactly what every AI is given
runs.json               one entry per run: which AI, when, how, caveats, raw file
raw/DATE/*.md           each AI's raw answer, untouched
data/responses.json     built by tools/build.py; the page reads this
tools/build.py          raw answers -> data
tools/run_headless.sh   the command-line runs (Codex, Grok, DeepSeek)
index.html              the page
```

## Adding a model

1. Give it `prompt.txt` cold (a new chat, no memory, nothing else pasted).
2. Save its answer untouched as `raw/DATE/<model>.md`.
3. Add a line to `runs.json`.
4. `python tools/build.py`, commit, push. The page updates itself.

## First run

2026-09-29, the day OpenAI released GPT-6.1 Sol: Claude Opus 5.5, Sonnet 5.5, Haiku 4.5, Fable 5.1, GPT-6 Luna,
GPT-6.1 Sol, Grok, and DeepSeek (twice).

The letter is almost a decoy. The reason is where the thinking shows, and "depends on perspective" only counts when the
reason behind it is specific.

CC0 - use it however you like.
