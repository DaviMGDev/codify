# Contributing to codify

Thanks for your interest in codify! This guide explains how to contribute
effectively — whether it's a typo fix, a spec proposal, or a new example.

## Project Philosophy

**codify is a set of conventions, not a compiler.** There is no build step, no
preprocessor, and no runtime. The entire project is Markdown documentation.

Read these before proposing changes:

- [`LANGUAGE.md`](LANGUAGE.md) — the full language specification
- [`README.md`](README.md) — project overview and status
- [ADR 001](docs/adr/001-drop-pseudo-extension-and-cli.md) — why we removed
  the CLI tool and `.pseudo` extension
- [ADR 002](docs/adr/002-duplicate-files-in-skill-bundle.md) — why the skill
  bundle intentionally duplicates `LANGUAGE.md` and `example.md`

**Key takeaway:** codify is intentionally loose. A proposal that adds strict
rules, type checking, or mandatory tooling is probably not a good fit. Proposals
that make the conventions clearer, more predictable, or more useful to LLMs are
always welcome.

## How to Propose a Change

### For small fixes (typos, broken links, formatting)

1. Open a PR directly. No issue needed.
2. Follow the [style guide](#style-guide) below.

### For spec changes, new constructs, or language design

1. **Open an issue first.** Describe what you want to change and why. Include
   examples of codify source that would be affected.
2. **Discuss before writing code.** Spec changes need alignment — a PR without
   prior discussion may be closed if it doesn't fit the philosophy.
3. If the change is architectural (changes project structure, affects the skill
   bundle, etc.), consider writing an [ADR](#architecture-decision-records).

### For bug reports (the skill produces wrong output, the spec is ambiguous)

1. Open an issue with:
   - The codify source that triggers the problem
   - What you expected the LLM to do
   - What it actually did
2. If possible, include which LLM you used (Claude, GPT, pi, etc.).

## Architecture Decision Records

Architectural decisions are documented as ADRs in [`docs/adr/`](docs/adr/).

### When to write an ADR

Write an ADR when a decision:
- Changes the project structure or tooling strategy
- Affects how contributors interact with the repo
- Introduces a new convention that future contributors must follow
- Reverses or supersedes a previous decision

### How to write an ADR

1. Copy [`docs/adr/template.md`](docs/adr/template.md) to
   `docs/adr/NNN-title-with-dashes.md` (where NNN is the next number).
2. Fill in all five sections: Status, Context, Decision, Consequences,
   Compliance.
3. Open a PR. ADRs are reviewed like any other change.

ADRs are **immutable** once accepted. To change a decision, write a new ADR
that supersedes the old one.

## Commit Conventions

This project follows [Conventional Commits](https://www.conventionalcommits.org/):

```
feat: add inline control flow syntax
docs: clarify prompt resolution in LANGUAGE.md
fix: correct loop variable scope in example
refactor: restructure skill SKILL.md
build: remove Python package scaffolding
```

### The `[skip-drift]` marker

The skill bundle intentionally duplicates two files from the repository root
(see [ADR 002](docs/adr/002-duplicate-files-in-skill-bundle.md)). A CI check
ensures these copies stay in sync.

If you intentionally change only one copy (which should be rare and
well-justified), include `[skip-drift]` in your commit message to bypass the
check:

```
docs: update LANGUAGE.md examples without skill bundle sync [skip-drift]
```

If the CI check fails unexpectedly, update the duplicate file to match and
push a new commit.

## Style Guide

- **Indentation:** 2 spaces, no tabs (enforced by [`.editorconfig`](.editorconfig))
- **Line endings:** LF (Unix)
- **Charset:** UTF-8
- **Language:** US English
- **Markdown:** Write for readability on GitHub. Use reference-style links for
  repeated URLs. Wrap long lines at ~100 characters when practical (not
  enforced).
- **File names:** lowercase with hyphens for documentation
  (`language-spec.md`), UPPERCASE for special files (`README.md`,
  `CHANGELOG.md`, `LICENSE`).

## Questions?

Open an issue on [GitHub](https://github.com/DaviMGDev/codify/issues). If
you're unsure whether something fits the project philosophy, ask before
investing time in a PR.
