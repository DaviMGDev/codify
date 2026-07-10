# codify

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Version](https://img.shields.io/badge/version-0.1.0-lightgrey)](LANGUAGE.md)
[![Status](https://img.shields.io/badge/status-draft-orange)]()

**codify** is a prompt-centric syntax system designed to be interpreted — and even written — by LLMs. Variables, control flow, functions, and embedded formats (YAML, JSON, TOML, Markdown) provide just enough structure for dynamic LLM-driven workflows, while staying loose enough that an LLM can produce valid codify without friction.

```txt
// answer each prompt in one sentence

name = "codify"
audience is developers and LLMs
version is 0.1.0

introduce name and state who it helps

tasks: yaml =
    parse: extract structured data from a log file
    summarize: write a 3-bullet summary of a PR

for task_name in tasks:
    estimate how long the task task_name should take

version is draft?
    what should stabilize before 0.2?
```

## Why codify?

| Problem | codify's answer |
|---------|-----------------|
| **Prompts get messy.** One-off instructions, copied context, version drift. | Variables and embedded data keep inputs in one place. Change a value once, the whole file updates. |
| **LLMs need structure.** A wall of text gets inconsistent results. | Control flow (`if` / `for`) and functions make branching and repetition explicit so the LLM follows the intended path. |
| **Reuse is hard.** Every prompt is a one-off; nothing is composable. | Functions act as reusable prompt templates. Declare once, call anywhere in the file. |

**When NOT to use codify:** your prompt is a single sentence, you need actual executable code, or you need strict validation (codify has no type checker).

## Getting started

1. **Write a `.md` file** using the conventions above — declarations, control flow, prompts.
2. **Paste the entire file** into any LLM (ChatGPT, Claude, pi, etc.).
3. **Done.** No install, no build step, no preprocessor.

See [`example.md`](example.md) for every construct in one file, or jump to [`LANGUAGE.md`](LANGUAGE.md) for the full spec.

## Language

codify is a set of conventions, not enforced rules. Any text that isn't a recognized construct is a natural-language **prompt** sent directly to the LLM.

| Construct | Syntax |
|-----------|--------|
| Comments | `//` single-line, `/* */` multi-line — read by the LLM as context and guidance |
| Declarations | `x = 10`, `pi is 3.14`, `me as user` — three equivalent styles |
| Type annotations | `person: adult = {...}`, `data: yaml = ...` — semantic labels, not enforced |
| Embedded formats | `: yaml =`, `: json =`, `: toml =`, `: xml =`, `: md =` — interpreted by the LLM |
| Control flow | `if condition:` (block) or `condition? action;` (inline) |
| Loops | `for item in iterator:` — iteration over lists, ranges, or natural-language descriptions |
| Functions | `fn name(args): type { ... }` or `def name(args) -> type:` — reusable prompt templates |
| Objects | `{ key: value }` — JSON-like, unquoted keys allowed |
| Lists | `[1, 2, 3]` |

Full specification: [`LANGUAGE.md`](LANGUAGE.md)

## Pi agent skill

A codify skill for [pi](https://github.com/Earendil-Works/pi-coding-agent) is included in this repo:

**[`skills/codify/SKILL.md`](skills/codify/SKILL.md)** — supports three modes:
- **Write** — author structured prompts using codify conventions
- **Review** — audit codify source for spec compliance, clarity, and LLM-friendliness
- **Convert** — translate between natural language and codify syntax in either direction

To use it, copy or symlink `skills/codify/` into your pi skills directory.

## Project status

| Area | Status |
|------|--------|
| Language spec | Draft — conventions defined in [`LANGUAGE.md`](LANGUAGE.md) |
| LLM skill (write, review, convert) | ✅ Implemented — [`skills/codify/SKILL.md`](skills/codify/SKILL.md) |
| Formatter | Planned |
| Syntax highlighting (TextMate / Tree-sitter) | Planned |

## Contributing

This is an early-stage solo project. Bug reports, spec proposals, and examples are welcome — open an issue or PR on [GitHub](https://github.com/DaviMGDev/codify).

Before proposing a language change, read [`LANGUAGE.md`](LANGUAGE.md) and the existing [ADRs](docs/adr/) for context on past decisions.

---

<div align="center">
MIT &mdash; 2026 Davi Macêdo Gomes
</div>
