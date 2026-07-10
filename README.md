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

### Status

Early draft. A comment stripper preprocessor is planned.
