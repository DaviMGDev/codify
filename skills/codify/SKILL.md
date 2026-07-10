---
name: codify
description: >-
  Write, review, and convert codify — a prompt-centric syntax system for
  LLM-driven workflows. Use when the user wants to structure prompts using
  codify conventions (variables, control flow, functions, embedded formats,
  hints). Supports fileless inline usage and file-based workflows via the
  codify CLI tool.
---

# Codify

A unified skill for the **codify** language — a prompt-centric syntax designed to be interpreted and written by LLMs. Codify provides just enough structure (variables, control flow, functions, hints, embedded formats) while keeping everything as prompt text the LLM interprets naturally.

Codify is a **syntax and convention system**, not a file format. Source files are conventionally stored as `.pseudo` and preprocessed into `.md` via the `codify strip -o` tool, but the skill works perfectly without any file at all — the syntax can be used directly in any prompt.

The skill has three operational modes:

| Mode | Function |
|------|----------|
| **write** | Author structured prompts using codify syntax; output as text inline, as `.md`, or via `codify strip -o` |
| **review** | Audit codify source (`.pseudo` or `.md`) for spec compliance, clarity, and LLM-friendliness |
| **convert** | Translate between natural language and codify syntax — no file required |

---

## When to use

- The user says: "write a codify prompt", "help me structure this task in codify", "create a codify workflow"
- The user says: "review this codify code", "check this .pseudo file", "is this valid codify?"
- The user says: "convert this prompt to codify", "explain this codify file in plain English", "translate this codify to natural language"
- The user shares a task description and wants it structured as codify constructs
- The user shares a `.pseudo` or `.md` file and wants it audited for correctness, ambiguities, or LLM-friendliness

---

## Context

Before using this skill, read these resource files bundled inside the skill directory:

| File | Why |
|------|-----|
| `references/LANGUAGE.md` | Full language spec — all constructs, conventions, and edge cases |
| `assets/examples/example.pseudo` | Reference file demonstrating every construct in one place |

### Key facts about codify

- **No compiler, no parser, no linter** — codify is a set of conventions, not enforced rules. Output is sent as one prompt to an LLM.
- **Everything is a prompt** — any text that isn't a comment, declaration, control flow construct, function, or embedded format is natural language sent to the LLM.
- **Fileless by default** — codify syntax can be used directly in any prompt without creating any file. When a file is needed, use `codify strip source.pseudo -o source.md` to preprocess.
- **Comments vs Hints**: `//` and `/* */` are stripped by the preprocessor (invisible to the LLM); `@` and `@*...*@` hints survive preprocessing as LLM meta-instructions.
- **Source extension**: `.pseudo` (conventional, not enforced)
- **Output extension**: `.md` (via `codify strip -o`)
- **No strict types** — type annotations like `: adult` or `: yaml` are semantic labels for the LLM, not enforced by any runtime.
- **Embedded formats** (YAML, TOML, JSON, XML, Markdown) are passed as-is to the LLM — the format annotation tells the LLM how to interpret the block.
- **CLI tool**: `codify strip` strips comments from a `.pseudo` source and prints clean text; with `-o FILE` it saves to that file instead of stdout.
- **Python 3.10+**, zero runtime dependencies, build system is Hatchling.

---

## Instructions

### Mode 1: Write Codify Syntax

Use this when the user asks to create structured prompts using codify conventions. The output can be delivered as text directly (fileless) or as a `.md` file (via `codify strip -o`).

#### Step 1: Determine delivery mode

Choose based on what the user needs:

- **Fileless (default)**: The user wants codify-structured prompts for use in a chat session, as a skill definition, or as part of a larger prompt. Convey the codify syntax directly in the response — no file created.
- **File-based**: The user wants a reusable file they can pass to an LLM later. Save codify source as `.pseudo`, then run `codify strip source.pseudo -o source.md` and deliver the `.md`.

Ask the user if unclear: "Do you want codify syntax as inline text, or as a `.md` file?"

#### Step 2: Identify the task scope

Determine what the codify content should accomplish. Ask the user if unclear:
- What is the single goal or question the LLM should answer?
- What data/context does the LLM need? (variables, embedded configs, lists)
- Should the output be structured? (control flow branching, loops over items)
- Are there behavioural instructions for the LLM? (use `@` hints for these)

#### Step 3: Structure the content

Organise the content top-to-bottom in this conventional order:

1. **Hints** (`@`) — Behavioral meta-instructions for the LLM (placed at top or inline)
2. **Declarations** — Variables, constants, data using `=`, `is`, or `as` style
3. **Embedded data** — Structured config in YAML, TOML, JSON, XML, or Markdown
4. **Functions** — Reusable prompt templates with `fn` or `def`
5. **Prompts** — The natural-language instructions/questions sent to the LLM
6. **Control flow / loops** — Branching and iteration over declared data

This order is a convention, not a rule — any construct can appear anywhere.

#### Step 4: Use correct construct syntax

Follow the syntax rules from `references/LANGUAGE.md`:

**Declarations** (three equivalent styles):
```
x = 10                          # assignment style
pi is 3.14                      # is style — reads naturally
me as user                      # as style — reads naturally
```

**Type annotations** (semantic labels for the LLM):
```
person: adult = {
    name: John
}
data: yaml =
    name: John
    age: 30
```

**Embedded formats** (annotated with format name):
```
config: yaml =
    theme: dark
    font: monospace

settings: toml =
    [editor]
    lineNumbers = true

user: json =
    {"role": "developer"}

data: xml =
    <items><item>one</item></items>

description: md =
    # Title
    **bold** text
```

**Control flow — block style** (colon + indentation):
```
if condition:
    do something
else if another condition:
    do something else
else:
    fallback action
```

**Control flow — inline style** (`?` and `;`):
```
condition? do this ; not condition? do that;
```

**Loops:**
```
for item in iterator:
    process item
```

**Functions:**
```
fn summarize(text: text) {
    summarize the input in 3 bullet points
}

def format_result(data: json) -> md:
    convert the json data to a markdown table
```

**Object notation** (curly braces, JSON-like):
```
repo = {
    name: codify,
    status: draft,
    license: MIT
}
```

**Lists:**
```
fruits = [apple, banana, cherry]
```

**Comments** (for humans — stripped by preprocessor):
```
// single-line comment
/* multi-line
   comment */
```

**Hints** (survive preprocessing as LLM meta-instructions):
```
@ give me a concise answer
@*
this hint spans
multiple lines
*@
```

#### Step 5: Place prompts as bare text

Any line that isn't one of the above constructs is a prompt — natural language sent directly to the LLM:

```
what is the capital of France?
how much is x + 5?
based on the data above, generate a summary
```

Prompts can reference variables declared earlier. The LLM resolves them in context.

#### Step 6 (file-based only): Preprocess to .md

When the user wants a file:
1. Save the codify source as `<name>.pseudo`
2. Run `codify strip <name>.pseudo -o <name>.md`
3. Present the `.md` as the deliverable.
   The intermediate `.pseudo` source can be discarded.

#### Step 7: Verify the content

- Read the content back and confirm every construct follows the syntax above
- Check that comments (`//`, `/* */`) are clearly distinguishable from hints (`@`, `@*...*@`)
- Check that embedded format annotations match the format of the content (e.g., `: yaml =` should precede YAML, not JSON)
- Check that control flow bodies are consistently indented (spaces or tabs, but not mixed)
- Check that `@` hints are on their own line and not mixed with prompts

---

### Mode 2: Review Codify Source

Use this when the user provides a codify snippet, `.pseudo` file, or `.md` file for audit.

#### Step 1: Read the source

Read the full content. For `.md` files, state the assumption that they originated from a codify source and check for embedded codify constructs (declarations, control flow, hints, etc.).

#### Step 2: Check construct syntax

Inspect each construct category:

| Construct | What to check |
|-----------|---------------|
| **Declarations** | `=`, `is`, `as` — are they on their own line? Is the variable name a single word (no spaces)? |
| **Type annotations** | Does the type label follow the `name: label =` pattern? For embedded formats, does the label match the format (`: yaml`, `: json`, etc.)? |
| **Control flow (block)** | Does the condition end with a colon? Is the body consistently indented? Are `else if` / `else` at the same indent level as `if`? |
| **Control flow (inline)** | Are conditions followed by `?` and branches separated by `;`? Can the LLM parse the chain? |
| **Loops** | Does `for ... in ...:` have a colon? Is the body indented? Is the iterator a range, a list variable, or a natural-language description? |
| **Functions** | Does `fn name(args) {` have a matching `}`? Is the body descriptive natural language (not implementation code)? |
| **Embedded formats** | Does the content following the annotation match the format? (e.g., YAML under `: yaml =`, JSON under `: json =`) |
| **Comments** | Are `//` only used BOL or after whitespace (so `https://` is not treated as a comment)? |
| **Hints** | Are `@` hints on their own line? Do multi-line hints use `@*...*@` (not nested `/* */`)? |

#### Step 3: Flag ambiguities

Look for constructs that could confuse an LLM:

- **Unclear scope**: Does a variable change meaning mid-file? (codify allows reassignment, but it can confuse the LLM.)
- **Mixed comment/hint intent**: Is the author using `//` when they mean `@` (i.e., writing a comment they want the LLM to see)?
- **Ambiguous control flow**: In inline style, are conditions and branches clearly delimited so the LLM can parse them?
- **Format mismatch**: Is there YAML-like content labeled `: json` or vice versa?
- **Missing annotations**: Is there embedded data without a format annotation, forcing the LLM to guess?
- **Overly long prompts**: Are there paragraphs of unstructured text that should be broken into variables + control flow?
- **Mixed indentation**: Are tabs and spaces mixed in indented blocks?

#### Step 4: Assess LLM-friendliness

Rate the content on these criteria:
- **Clarity**: Would an LLM immediately understand the task from the prompts?
- **Structure**: Are related data grouped via embedded formats? Are branching paths explicit?
- **Hint quality**: Do `@` hints set clear behavioural expectations for the LLM?
- **Redundancy**: Are prompts repeating information already declared in variables?

#### Step 5: Report findings

Present the review as a structured report:

```markdown
## Review: `<filename>`

### ✅ Pass
- [list of correctly used constructs]

### ⚠️ Issues
| Severity | Finding | Line(s) | Suggestion |
|----------|---------|---------|------------|
| low/med/high | description | 12–15 | fix suggestion |
```

---

### Mode 3: Convert Codify ↔ Natural Language

Use this when the user wants to translate between formats in either direction. No file is required at any step — codify syntax is text.

#### Direction A: Codify → Natural Language

Explain what a codify source instructs the LLM to do.

1. **Read the full source** (`.pseudo`, `.md`, or inline snippet).
2. **Identify all constructs** — declarations, hints, embedded data, functions, control flow, loops.
3. **Trace the prompt sequence** — read the natural-language prompts in order, resolving variable references where they appear.
4. **Summarise the intent**: "This codify source asks the LLM to [goal]. It provides [data] and instructs the LLM to [actions]."
5. **Map constructs to plain English**:
   - Variables → "It defines X as Y"
   - Hints → "The LLM is instructed to [behaviour]"
   - Control flow → "If [condition], the LLM should [action]; otherwise [alternative]"
   - Loops → "For each [item], the LLM should [action]"
   - Functions → "The LLM can be called with [parameters] to produce [result]"
   - Embedded formats → "Structured data is provided in [format]"

#### Direction B: Natural Language → Codify

Convert a task description into structured codify constructs. Output the codify syntax as text — no file required.

1. **Parse the task** — Identify:
   - The core question or goal (→ becomes one or more prompts)
   - Data/context provided (→ becomes declarations or embedded formats)
   - Conditions or branching logic (→ becomes control flow)
   - Repetitive elements (→ becomes loops)
   - Reusable sub-tasks (→ becomes functions)
   - Behavioural instructions for the LLM (→ becomes `@` hints)

2. **Structure the output** following the conventional order (hints → declarations → embedded data → functions → prompts → control flow).

3. **Choose declaration style** based on readability:
   - Use `=` for programmatic values
   - Use `is` for natural-language-like statements
   - Use `as` for roles or identity mappings

4. **Choose control flow style** based on complexity:
   - Use block style (colon + indent) for 2+ branches or nested conditions
   - Use inline style (`?` and `;`) for simple binary conditions

5. **Place behavioural instructions as `@` hints** at the top.

6. **Verify round-trip clarity** — the codify output should be understandable by an LLM without additional context.

---

## Examples

### Write — Fileless (inline syntax)

**User request:** "Create a codify prompt that asks the LLM to analyse a list of products and recommend the best one based on price and rating."

**Output (inline — no file created):**
```
@ be concise and justify each recommendation with data

products = [
    { name: "Widget A", price: 29, rating: 4.5 },
    { name: "Widget B", price: 49, rating: 4.8 },
    { name: "Widget C", price: 15, rating: 3.9 }
]

threshold: yaml =
    max_price: 40
    min_rating: 4.0

for product in products:
    evaluate product based on price and rating
    if product meets the threshold:
        mark as recommended
    else:
        note why it falls short

which products meet the threshold? recommend the best value option and explain why.
```

### Write — File-based (with codify strip -o)

**User request:** "Make a codify workflow file for analysing sample data."

**Process:**
1. Draft the codify source as `analysis.pseudo`
2. Run `codify strip analysis.pseudo -o analysis.md`
3. Deliver `analysis.md`

### Review — Auditing a codify snippet

**User request:** "Check this codify snippet."

**Input:**
```
x=10
// this is a note for the LLM
how much is x?
```

**Review output:**
```
## Review: snippet

### ✅ Pass
- Prompt correctly references variable x

### ⚠️ Issues
| Severity | Finding | Line(s) | Suggestion |
|----------|---------|---------|------------|
| high | `//` comment will be stripped by preprocessor — LLM won't see it. If the LLM should see it, use `@` instead. | 2 | Change `//` to `@` |
| low | Missing space around `=`. Works, but inconsistent with spec conventions. | 1 | Add spaces: `x = 10` |
```

### Convert — Codify → Natural Language

**Input:**
```
@ respond in a friendly tone

name = "Alice"
role is engineer

greet name and acknowledge role
```

**Output:**
> This codify source asks the LLM to greet someone named Alice and acknowledge that they are an engineer. It sets an `@` hint telling the LLM to use a friendly tone. A variable `name` is defined as "Alice" and `role` is defined as "engineer" using the `is` style. The prompt asks the LLM to greet the person by name and acknowledge their role.

### Convert — Natural Language → Codify

**User request:** "I want the LLM to check if a number is even or odd and respond accordingly."

**Output (inline — no file):**
```
@ respond with just "even" or "odd", no extra text

number = 7

number % 2 == 0? respond with "even";
not number % 2 == 0? respond with "odd";
```

---

## Edge Cases & Gotchas

| Situation | Guidance |
|-----------|----------|
| **`https://` mistaken for comment** | The comment stripper only treats `//` as a comment when preceded by whitespace or BOL. In `https://`, the `//` follows `:` so it's left as text. When writing codify, avoid writing `//` mid-word to prevent LLM misinterpretation. |
| **Unclosed `/*` at EOF** | The preprocessor raises a `ValueError`. Always close multi-line comments. |
| **Nested comments** | `/* /* */ */` is not supported — the first `*/` closes the entire comment. Avoid nesting `/* */` inside `/* */`. |
| **`@` hints mixed with prompts** | `@` must be on its own line to be treated as a hint. If `@` appears mid-prompt, the preprocessor may not handle it correctly — keep hints isolated. |
| **Whitespace in variable names** | Variable names must be single tokens (no spaces). Use `snake_case` or `camelCase`. |
| **Inline control flow chaining** | Long inline chains (`condition? a; not condition? another? b; else c;`) can confuse the LLM. Prefer block style for 3+ branches. |
| **Type annotations ≠ validation** | Types like `: yaml` or `: adult` are purely semantic labels for the LLM. The preprocessor does not validate embedded format syntax. |
| **Reassignment** | codify allows reassignment (`x = 10` then later `x = 20`), but this can confuse the LLM. Flag reassignment during review — suggest unique variable names. |
| **Mixed indentation** | Block-structured constructs (control flow, loops, functions) require consistent indentation. Mixing tabs and spaces degrades LLM parsing. |
| **Functions as prompt templates** | Functions are not executable code — they are reusable descriptions of behaviour. Do not expect them to be called with concrete arguments like a real function. |
| **Fileless vs file-based** | When the user just wants codify syntax, deliver it as text inline. Only use a `.pseudo` source with `codify strip -o` when the user explicitly asks for a reusable file. |
