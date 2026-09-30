# AI Framing Study

**See it:** https://jaronkbragg7337.github.io/AI-Framing-Study/

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
