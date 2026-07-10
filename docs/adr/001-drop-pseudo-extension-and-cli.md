# ADR 001: Drop `.pseudo` file extension and remove the CLI tool

**Status:** Accepted

**Context:**
The codify language was originally associated with a `.pseudo` file extension
and shipped with a CLI tool (`codify strip`) that stripped `//` and `/* */`
comments from source files before sending them to an LLM. This created several
problems:

- AI tools and LLMs placed disproportionate importance on the `.pseudo`
  extension, treating it as a rigid format requirement rather than a convention.
- The CLI tool suggested a preprocessing pipeline was necessary for codify to
  work, which is false — codify is a syntax convention interpreted by LLMs
  directly, with no compilation or preprocessing step required.
- Maintaining the preprocessor added friction with no real benefit: the LLM
  can understand `//` and `/* */` comments natively without a stripping step.

**Decision:**
1. Abandon the `.pseudo` file extension entirely. Codify syntax works in any
   text file — no special extension is needed.
2. Remove the entire CLI tool (`cli.py`, `__main__.py`, CLI entry point in
   `pyproject.toml`, and all references to `codify strip` in documentation).
3. Remove all build artifacts and Python tooling (`.venv/`, `uv.lock`,
   `__pycache__/`, `dist/`, `*.egg-info/`) since the project no longer ships
   executable code.
4. Strip all references to `.pseudo` and the preprocessor from the language
   spec (`LANGUAGE.md`), the skill definition (`SKILL.md`), and documentation
   (`README.md`).
5. Rename `example.pseudo` to `example.md` and update all cross-references.

**Consequences:**
- Positive: The project is now purely a specification + documentation project.
  No build, no install, no preprocessor — just a language definition and
  examples.
- Positive: AI agents and LLMs no longer fixate on a file extension. Codify
  syntax is usable in any `.md` file or directly in a prompt.
- Positive: Reduced maintenance burden — no CLI code to test, no dependencies
  to update, no build pipeline.
- Negative: Users who relied on the CLI for comment stripping must find
  alternative approaches (or ignore comments — the LLM handles them fine).
- Negative: Users familiar with `.pseudo` must adjust to extensionless codify
  files.

**Compliance:**
- No file in the repository references `.pseudo` as a meaningful extension
  (the ADR file itself and AGENTS.md are exempted — they describe the
  decision).
- No file references a CLI tool or preprocessor.
- No build artifacts (`.venv/`, `uv.lock`, `__pycache__/`, `dist/`,
  `*.egg-info/`) exist in the repository.
- The `pyproject.toml` no longer declares a CLI entry point or scripts
  section.
