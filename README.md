# codify

**codify** is a prompt-centric DSL designed to be interpreted — and even written — by LLMs.

The language is intentionally loose: a set of conventions that define better agent behavior without enforcing strict rules. Any text that isn't a language construct is a prompt. Variables, control flow, functions, and embedded formats (JSON, YAML, TOML, Markdown) provide just enough structure for dynamic, LLM-driven workflows while staying flexible enough that an LLM can produce valid code without friction.

```
x = 10
how much is x?
```

```txt
fn summarize(text: text) {
    summarize the following in 3 bullet points
}
```

### Philosophy

- No compiler, no LSP, no linter, no type checker
- Conventions, not rules — recommendations, not enforcement
- The entire file is **one prompt** sent to an LLM
- The LLM interprets structure from context

### File format

```
*.pseudo     # codify source files
```

---

## Installation

```bash
pip install git+https://github.com/davigomes404/codify.git
```

Or from a local clone:

```bash
git clone https://github.com/davigomes404/codify.git
cd codify
pip install .
```

Requires Python 3.10+.

## Usage

### `codify strip` — Strip comments from `.pseudo` files

Removes `//` and `/* */` comments while preserving `@` hints (which survive preprocessing as meta-instructions to the LLM).

```bash
codify strip example.pseudo
```

Read from stdin:

```bash
cat example.pseudo | codify strip
```

**Before** (`example.pseudo`):

```
// this comment is stripped
@ this hint survives

x = 10
how much is x?
```

**After** (`codify strip example.pseudo`):

```
@ this hint survives

x = 10
how much is x?
```

### `python -m codify`

The package also runs as a module for environments where the CLI script is unavailable:

```bash
python -m codify strip example.pseudo
```

## Language Specification

See [`LANGUAGE.md`](LANGUAGE.md) for the full language draft — declarations, control flow, loops, functions, embedded formats (YAML, JSON, TOML, XML, Markdown), and the `@` hint system.

## Example

[`example.pseudo`](example.pseudo) demonstrates every codify construct in one file. Run `codify strip example.pseudo` to see the prompt that gets sent to the LLM.

## Project Status

| Area | Status |
|------|--------|
| Language spec | Draft — stable conventions defined in `LANGUAGE.md` |
| Comment stripper (`codify strip`) | ✅ Implemented |
| Formatter | Planned |
| Syntax highlighting (TextMate / Tree-sitter) | Planned |
| LLM skills (write, review, convert) | Planned |

---

<div align="center">
MIT &mdash; 2026 Davi Macêdo Gomes
</div>
