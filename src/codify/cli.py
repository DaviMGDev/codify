"""codify strip — strip // and /* */ comments from codify source files."""

import argparse
import sys
from pathlib import Path


def strip_comments(text: str) -> str:
    """Strip // and /* */ comments from *text*.

    Rules:
    - ``//`` starts a single-line comment only when preceded by whitespace or
      start-of-line (so ``https://`` is left alone).
    - ``/* ... */`` is a multi-line comment. Nesting is not supported — the
      first ``*/`` closes the comment.
    - An unclosed ``/*`` at EOF raises ``ValueError``.
    """

    out: list[str] = []
    i = 0
    n = len(text)
    # State machine: CODE, SAW_SLASH, LINE_COMMENT, MULTI_COMMENT, SAW_STAR
    state = "CODE"
    # The character before the current position — used to decide if '//'
    # is a comment (only when preceded by whitespace or start-of-line).
    prev: str | None = None

    while i < n:
        ch = text[i]

        if state == "CODE":
            if ch == "/":
                state = "SAW_SLASH"
            else:
                out.append(ch)
                prev = ch
            i += 1

        elif state == "SAW_SLASH":
            if ch == "/":
                # '//' comment only if preceded by whitespace or BOL
                if prev is None or prev.isspace():
                    state = "LINE_COMMENT"
                else:
                    out.append("/")
                    out.append(ch)
                    prev = ch
                    state = "CODE"
            elif ch == "*":
                state = "MULTI_COMMENT"
            else:
                out.append("/")
                out.append(ch)
                prev = ch
                state = "CODE"
            i += 1

        elif state == "LINE_COMMENT":
            if ch == "\n":
                out.append("\n")
                state = "CODE"
                prev = "\n"
            i += 1

        elif state == "MULTI_COMMENT":
            if ch == "*":
                state = "SAW_STAR"
            i += 1

        elif state == "SAW_STAR":
            if ch == "/":
                state = "CODE"
                # prev stays — don't reset it
            elif ch == "*":
                pass  # stay in SAW_STAR for "***/"
            else:
                state = "MULTI_COMMENT"
            i += 1

    # Cleanup after the loop
    if state in ("MULTI_COMMENT", "SAW_STAR"):
        raise ValueError("unclosed multi-line comment at end of file")
    if state == "SAW_SLASH":
        out.append("/")  # orphan '/' at EOF

    return "".join(out)


def run_strip(args: argparse.Namespace) -> None:
    """Handle the *strip* subcommand: read, strip, print."""
    try:
        if args.file and args.file != "-":
            text = Path(args.file).read_text(encoding="utf-8")
        else:
            text = sys.stdin.read()
    except FileNotFoundError:
        print(f"error: file not found: {args.file}", file=sys.stderr)
        sys.exit(1)
    except UnicodeDecodeError as exc:
        print(f"error: invalid UTF-8 in {args.file}: {exc}", file=sys.stderr)
        sys.exit(1)

    try:
        result = strip_comments(text)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        sys.exit(1)

    if args.output:
        try:
            Path(args.output).write_text(result, encoding="utf-8")
        except OSError as exc:
            print(f"error: cannot write to {args.output}: {exc}", file=sys.stderr)
            sys.exit(1)
    else:
        sys.stdout.write(result)


def build_parser() -> argparse.ArgumentParser:
    """Build the argument parser."""
    parser = argparse.ArgumentParser(
        prog="codify",
        description="codify — a prompt-centric DSL toolchain.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    strip_parser = sub.add_parser("strip", help="Strip comments from a codify source file")
    strip_parser.add_argument(
        "file",
        nargs="?",
        default="-",
        help="Path to .pseudo file (default: stdin)",
    )
    strip_parser.add_argument(
        "-o",
        "--output",
        help="Write output to FILE instead of stdout (e.g., .md)",
        metavar="FILE",
    )
    strip_parser.set_defaults(func=run_strip)

    return parser


def main() -> None:
    """Entry point for the CLI."""
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
