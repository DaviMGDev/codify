# Changelog

All notable changes to the codify project are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Conventional Commits](https://www.conventionalcommits.org/).

## [Unreleased]

## [0.1.0] — 2026-07-10

### Added
- Language specification (`LANGUAGE.md`) covering comments, prompts, declarations,
  types, embedded formats (YAML/TOML/JSON/XML/Markdown), control flow, loops,
  lists, functions, and object notation.
- Reference example (`example.md`) demonstrating every language construct.
- Pi-agent skill (`skills/codify/SKILL.md`) supporting three modes: write,
  review, and convert codify ↔ natural language.
- Architecture Decision Record process (`docs/adr/`).
- Project README with quickstart guide and constructs table.

### Changed
- Language renamed to "codify".
- Skill reframed from file-format tool to syntax system — codify works
  filelessly in any text prompt.

### Removed
- `.pseudo` file extension — codify works in `.md` or any text file.
- CLI comment stripper (`codify strip`) — codify has no preprocessor;
  comments are interpreted directly by the LLM.
- Python package scaffolding (`pyproject.toml`, `cli.py`, `uv.lock`,
  `.venv/`) — the project is now pure documentation with zero dependencies.
- `@hint` convention — replaced by standard `//` and `/* */` comments.

[0.1.0]: https://github.com/DaviMGDev/codify/releases/tag/v0.1.0
