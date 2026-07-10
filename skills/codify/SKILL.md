---
name: codify
description: >-
  Write, review, and convert codify — a prompt-centric syntax system for
  LLM-driven workflows. Use when the user wants to structure prompts using
  codify conventions (variables, control flow, functions, embedded formats,
  hints). Supports fileless inline usage and file-based workflows.
---

# Codify

A unified skill for the **codify** language — a prompt-centric syntax designed to be interpreted and written by LLMs. Codify provides just enough structure (variables, control flow, functions, comments, embedded formats) while keeping everything as prompt text the LLM interprets naturally.

Codify is a **syntax and convention system**, not a file format. The syntax works in any text file — no special extension or preprocessing step is needed.

The skill has three operational modes:

modes: yaml =
  write: Author structured prompts using codify syntax; output as text inline
  review: Audit codify source for spec compliance, clarity, and LLM-friendliness
  convert: Translate between natural language and codify syntax — no file required

---

## When to use

when_to_use = [
  "user says: write a codify prompt, help me structure this task in codify, create a codify workflow",
  "user says: review this codify code, check this codify file, is this valid codify?",
  "user says: convert this prompt to codify, explain this codify file in plain English, translate this codify to natural language",
  "user shares a task description and wants it structured as codify constructs",
  "user shares a codify source file and wants it audited for correctness, ambiguities, or LLM-friendliness"
]

---

## Context

Before using this skill, read these resource files bundled inside the skill directory:

| File | Why |
|------|-----|
| `references/LANGUAGE.md` | Full language spec — all constructs, conventions, and edge cases |
| `assets/examples/example.md` | Reference file demonstrating every construct in one place |

### Key facts about codify

key_facts: yaml =
  no_compiler: codify is a set of conventions, not enforced rules. Output is sent as one prompt to an LLM.
  everything_is_prompt: any text that is not a comment, declaration, control flow construct, function, or embedded format is natural language sent to the LLM.
  fileless_by_default: codify syntax can be used directly in any prompt without creating any file.
  comments: "// and /* */ are read by the LLM as context, guidance, and meta-instructions."
  no_file_extension: codify syntax works in any text file. No special extension is needed.
  no_strict_types: "type annotations like :adult or :yaml are semantic labels for the LLM, not enforced by any runtime."
  embedded_formats: "YAML, TOML, JSON, XML, Markdown are passed as-is to the LLM — the format annotation tells the LLM how to interpret the block."

---

## Instructions

### Mode 1: Write Codify Syntax

Use this when the user asks to create structured prompts using codify conventions. Codify syntax is delivered as text directly — no file creation or preprocessing step is needed.

#### Step 1: Identify the task scope

Determine what the codify content should accomplish. Ask the user if unclear.

scope_questions = [
  "What is the single goal or question the LLM should answer?",
  "What data/context does the LLM need? (variables, embedded configs, lists)",
  "Should the output be structured? (control flow branching, loops over items)",
  "Are there behavioural instructions for the LLM? (use comments for these)"
]

for question in scope_questions:
    if answer is unclear: ask the user

#### Step 2: Structure the content

Organise the content top-to-bottom in this conventional order.

structure_order = [
  "Declarations — Variables, constants, data using =, is, or as style",
  "Embedded data — Structured config in YAML, TOML, JSON, XML, or Markdown",
  "Functions — Reusable prompt templates with fn or def",
  "Prompts — The natural-language instructions/questions sent to the LLM",
  "Control flow / loops — Branching and iteration over declared data"
]

// This order is a convention, not a rule — any construct can appear anywhere.

#### Step 3: Use correct construct syntax

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

**Comments** (context, guidance, and meta-instructions for the LLM):
```
// concise answer only, no preamble
// the user prefers dark mode
/* this section handles
   the export workflow */
```

#### Step 4: Place prompts as bare text

Any line that isn't one of the above constructs is a prompt — natural language sent directly to the LLM:

```
what is the capital of France?
how much is x + 5?
based on the data above, generate a summary
```

Prompts can reference variables declared earlier. The LLM resolves them in context.

#### Step 5: Verify the content

verification_checks = [
  "read the content back and confirm every construct follows the syntax above",
  "check that comments use // or /* */ syntax consistently",
  "check that embedded format annotations match the format of the content (e.g., : yaml = should precede YAML, not JSON)",
  "check that control flow bodies are consistently indented (spaces or tabs, but not mixed)"
]

for check in verification_checks:
    perform check

---

### Mode 2: Review Codify Source

Use this when the user provides a codify snippet or source file for audit.

#### Step 1: Read the source

Read the full content.

#### Step 2: Check construct syntax

Inspect each construct category:

construct_checks: yaml =
  declarations: "=, is, as — are they on their own line? Is the variable name a single word (no spaces)?"
  type_annotations: "Does the type label follow the name: label = pattern? For embedded formats, does the label match the format (: yaml, : json, etc.)?"
  control_flow_block: "Does the condition end with a colon? Is the body consistently indented? Are else if / else at the same indent level as if?"
  control_flow_inline: "Are conditions followed by ? and branches separated by ;? Can the LLM parse the chain?"
  loops: "Does for ... in ...: have a colon? Is the body indented? Is the iterator a range, a list variable, or a natural-language description?"
  functions: "Does fn name(args) { have a matching }? Is the body descriptive natural language (not implementation code)?"
  embedded_formats: "Does the content following the annotation match the format? (e.g., YAML under : yaml =, JSON under : json =)"
  comments: "Are // only used BOL or after whitespace (so https:// is not mistaken for a comment)?"

#### Step 3: Flag ambiguities

Look for constructs that could confuse an LLM:

ambiguities_to_flag = [
  "Unclear scope: Does a variable change meaning mid-file? (codify allows reassignment, but it can confuse the LLM.)",
  "Ambiguous control flow: In inline style, are conditions and branches clearly delimited so the LLM can parse them?",
  "Format mismatch: Is there YAML-like content labeled : json or vice versa?",
  "Missing annotations: Is there embedded data without a format annotation, forcing the LLM to guess?",
  "Overly long prompts: Are there paragraphs of unstructured text that should be broken into variables + control flow?",
  "Mixed indentation: Are tabs and spaces mixed in indented blocks?"
]

for ambiguity in ambiguities_to_flag:
    look for ambiguity in source

#### Step 4: Assess LLM-friendliness

Rate the content on these criteria:
llm_friendliness_criteria = [
  "Clarity: Would an LLM immediately understand the task from the prompts?",
  "Structure: Are related data grouped via embedded formats? Are branching paths explicit?",
  "Comment quality: Do comments set clear behavioural expectations and provide useful context for the LLM?",
  "Redundancy: Are prompts repeating information already declared in variables?"
]

for criterion in llm_friendliness_criteria:
    rate source against criterion

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

1. **Read the full source** (codify source file or inline snippet).
2. **Identify all constructs** — declarations, embedded data, functions, control flow, loops.
3. **Trace the prompt sequence** — read the natural-language prompts in order, resolving variable references where they appear.
4. **Summarise the intent**: "This codify source asks the LLM to [goal]. It provides [data] and instructs the LLM to [actions]."
5. **Map constructs to plain English**:
   - Variables → "It defines X as Y"
   - Comments → "The LLM is instructed to [behaviour]"
   - Control flow → "If [condition], the LLM should [action]; otherwise [alternative]"
   - Loops → "For each [item], the LLM should [action]"
   - Functions → "The LLM can be called with [parameters] to produce [result]"
   - Embedded formats → "Structured data is provided in [format]"

#### Direction B: Natural Language → Codify

Convert a task description into structured codify constructs. Output the codify syntax as text — no file required.

fn nl_to_codify(task: text) {
    1. parse task — identify:
       core question or goal → becomes one or more prompts
       data/context provided → becomes declarations or embedded formats
       conditions or branching logic → becomes control flow
       repetitive elements → becomes loops
       reusable sub-tasks → becomes functions
       behavioural instructions for LLM → use comments

    2. structure output following conventional order (declarations → embedded data → functions → prompts → control flow)

    3. choose declaration style based on readability:
       use = for programmatic values
       use is for natural-language-like statements
       use as for roles or identity mappings

    4. choose control flow style based on complexity:
       use block style (colon + indent) for 2+ branches or nested conditions
       use inline style (? and ;) for simple binary conditions

    5. verify round-trip clarity — codify output should be understandable by LLM without additional context
}

---

## Examples

### Write — Fileless (inline syntax)

**User request:** "Create a codify prompt that asks the LLM to analyse a list of products and recommend the best one based on price and rating."

**Output (inline — no file created):**
```
// be concise and justify each recommendation with data

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
| low | Missing space around `=`. Works, but inconsistent with spec conventions. | 1 | Add spaces: `x = 10` |
```

### Convert — Codify → Natural Language

**Input:**
```
// respond in a friendly tone

name = "Alice"
role is engineer

greet name and acknowledge role
```

**Output:**
> This codify source asks the LLM to greet someone named Alice and acknowledge that they are an engineer. A comment tells the LLM to use a friendly tone. A variable `name` is defined as "Alice" and `role` is defined as "engineer" using the `is` style. The prompt asks the LLM to greet the person by name and acknowledge their role.

### Convert — Natural Language → Codify

**User request:** "I want the LLM to check if a number is even or odd and respond accordingly."

**Output (inline — no file):**
```
// respond with just "even" or "odd", no extra text

number = 7

number % 2 == 0? respond with "even";
not number % 2 == 0? respond with "odd";
```

---

## Edge Cases & Gotchas

edge_cases: yaml =
  https_comment: "Avoid writing // mid-word to prevent LLM misinterpretation."
  unclosed_block: "Always close multi-line comments."
  nested_comments: "/* /* */ */ is not supported — the first */ closes the entire comment. Avoid nesting /* */ inside /* */."
  whitespace_names: "Variable names must be single tokens (no spaces). Use snake_case or camelCase."
  inline_chaining: "Long inline chains can confuse the LLM. Prefer block style for 3+ branches."
  annotations_not_validation: "Types like :yaml or :adult are purely semantic labels for the LLM."
  reassignment: "codify allows reassignment (x = 10 then later x = 20), but this can confuse the LLM. Flag reassignment during review — suggest unique variable names."
  mixed_indentation: "Block-structured constructs require consistent indentation. Mixing tabs and spaces degrades LLM parsing."
  functions_as_templates: "Functions are not executable code — they are reusable descriptions of behaviour."
