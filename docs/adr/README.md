# Architecture Decision Records

This directory contains Architecture Decision Records (ADRs) for the codify
project.

## What is an ADR?

An ADR captures a significant architectural decision, the context in which it
was made, and its consequences. ADRs are **immutable** once accepted — to change
a decision, write a new ADR that supersedes the old one.

Learn more at [adr.github.io](https://adr.github.io/).

## Index

| # | Title | Status |
|---|-------|--------|
| [001](001-drop-pseudo-extension-and-cli.md) | Drop `.pseudo` file extension and remove CLI tool | ✅ Accepted |
| [002](002-duplicate-files-in-skill-bundle.md) | Duplicate files in skill bundle are intentional | ✅ Accepted |

## Process

1. Copy [`template.md`](template.md) to `NNN-title-with-dashes.md` (use the
   next available number).
2. Fill in all five sections:
   - **Status** — Start with `Proposed`. Change to `Accepted` after review.
   - **Context** — What problem are we solving? What constraints exist?
   - **Decision** — What did we choose and why?
   - **Consequences** — What gets easier? What gets harder?
   - **Compliance** — How do we verify this decision is followed?
3. Open a PR. ADRs are reviewed like any other change.
4. Once accepted, update the index above.

### Statuses

| Status | Meaning |
|--------|---------|
| `Proposed` | Under discussion in a PR |
| `Accepted` | Approved and in effect |
| `Deprecated` | No longer applies (see superseding ADR) |
| `Superseded` | Replaced by a newer ADR |
