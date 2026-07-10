# ADR 002: Duplicate files in skill bundle are intentional

**Status:** Accepted

**Context:**
The repository contains two pairs of byte-identical files:

| Root file | Skill bundle copy |
|-----------|-------------------|
| `LANGUAGE.md` | `skills/codify/references/LANGUAGE.md` |
| `example.md` | `skills/codify/assets/examples/example.md` |

This duplication is visible to anyone diffing the repo and may appear to be
an oversight — suggesting symlinks or deduplication as a fix. In most
software projects, duplicate files are a maintenance hazard and should be
eliminated. However, the relationship between the codify repository and the
skill bundle makes this duplication both intentional and necessary.

**Decision:**
The duplicates **must remain** as they are. They will not be replaced with
symlinks, relative path references, or any other deduplication mechanism.

**Rationale:**

1. **The skill bundle must be self-contained.** When an agent installs a
   skill, it copies only the skill directory (`skills/codify/`) — not the
   entire repository. If the skill referenced root files via relative paths
   (e.g., `../../LANGUAGE.md`), those references would break at install time
   because the root files would not be present in the installed skill
   directory.

2. **Symlinks do not survive distribution.** The skill may be distributed as
   a tarball, a zip archive, or a git sparse checkout. Symlinks are
   unreliable across platforms and packaging formats. A plain copy is the
   only distribution format that works universally.

3. **The repository and the skill serve different audiences.** The repository
   root files (`LANGUAGE.md`, `example.md`) target human readers browsing
   GitHub. The skill bundle copies target the LLM agent that loads the skill
   at runtime. These are separate consumption contexts that happen to need
   the same content.

4. **The duplication surface is small and stable.** Two files totaling ~430
   lines. The language spec and the example evolve slowly (the spec is a
   draft, but its core constructs are unlikely to change frequently). The
   maintenance cost of keeping two copies in sync is negligible compared to
   the correctness risk of broken references at install time.

5. **Alternatives considered:**
   - *Symlinks:* Rejected — break on most distribution paths (tarball, zip,
     cross-platform).
   - *Relative path references in SKILL.md:* Rejected — the SKILL.md
     instructs the LLM to read `references/LANGUAGE.md`; changing this to a
     relative path outside the skill directory would break when the skill is
     installed standalone.
   - *Build step to copy files:* Rejected — adds complexity to a project
     whose core philosophy is "no build step, no preprocessor" (see ADR 001).
   - *Single copy in skill, remove from root:* Rejected — the root repo
     should remain browsable and self-explanatory on GitHub without
     descending into `skills/codify/`.

**Consequences:**

- Positive: The skill bundle remains fully self-contained and portable. Any
  agent can install it by copying the `skills/codify/` directory alone.
- Positive: The root repository remains independently browsable — no file in
  the root depends on content buried inside the skill directory.
- Positive: No build step, no symlink fragility, no distribution surprises.
- Negative: Changes to `LANGUAGE.md` or `example.md` must be applied to both
  copies. This is two files, well under 500 lines total — the overhead is
  minimal. A CI check can detect drift if desired.
- Negative: Tooling that flags duplicate files (linters, analysis scripts)
  will flag these as false positives. This ADR serves as the documented
  reason to suppress those warnings.

**Compliance:**
- Both file pairs remain byte-identical or intentionally diverged when one
  context needs different content.
- No symlinks exist for these files.
- The SKILL.md references `references/LANGUAGE.md` and
  `assets/examples/example.md` — paths that resolve correctly within the
  self-contained skill directory.
- If a CI drift check is added, it should reference this ADR as the
  authoritative explanation for the intentional duplication.
