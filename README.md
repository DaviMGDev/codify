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

## Language Specification

See [`LANGUAGE.md`](LANGUAGE.md) for the full language draft — declarations, control flow, loops, functions, embedded formats (YAML, JSON, TOML, XML, Markdown), and the `@` hint system.

## Example

[`example.md`](example.md) demonstrates every codify construct in one file.

## Project Status

| Area | Status |
|------|--------|
| Language spec | Draft — stable conventions defined in `LANGUAGE.md` |
| Formatter | Planned |
| Syntax highlighting (TextMate / Tree-sitter) | Planned |
| LLM skills (write, review, convert) | Planned |

---

<div align="center">
MIT &mdash; 2026 Davi Macêdo Gomes
</div>
