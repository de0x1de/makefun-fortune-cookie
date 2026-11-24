#!/usr/bin/env python3
"""Write the fortune-cookie entry for Fortune Cookie Wisdom for Developers.

The entry is one original fortune-cookie line for a software
developer, at most 120 characters.  This program assembles that
line from its parts, validates the result, writes it to
/output/entry.txt as UTF-8 with no trailing newline, and reads
it back for a byte-for-byte comparison.
"""

import os
import sys

OUTPUT_PATH = "/output/entry.txt"
MAX_LENGTH = 120

# The fortune is built from its parts rather than stored as one
# literal: a proverb-style opening names the developer who acts,
# a middle clause states what that act earns him, and a closing
# clause names the duty he was trying to get away from.  Joined
# with single spaces, the parts form the cookie's one sentence.
OPENING_WORDS = ("He", "who", "restarts", "the", "server", "at", "midnight")
EARNING_WORDS = ("shall", "inherit", "the", "on-call")
ESCAPE_WORDS = ("he", "tried", "to", "escape.")


def assemble_fortune() -> str:
    """Join the fortune's three clauses into a single line."""
    clauses = (
        " ".join(OPENING_WORDS),
        " ".join(EARNING_WORDS),
        " ".join(ESCAPE_WORDS),
    )
    return " ".join(clauses)


def validate_fortune(text: str) -> None:
    """Raise ValueError if the assembled line breaks any rule."""
    if not text or not text.strip():
        raise ValueError("fortune must not be empty or only whitespace")
    if len(text) > MAX_LENGTH:
        raise ValueError(
            f"fortune must be at most {MAX_LENGTH} characters, got {len(text)}"
        )
    if len(text) < 1:
        raise ValueError("fortune must contain at least one character")
    if "\n" in text or "\r" in text:
        raise ValueError("fortune must be a single line with no newline")
    if text != text.strip():
        raise ValueError("fortune must not have leading or trailing space")
    if "  " in text:
        raise ValueError("fortune must use single spaces between words")
    if not text.endswith("."):
        raise ValueError("fortune must end with a full stop")
    if text.count(".") != 1:
        raise ValueError("fortune must be one sentence with a single full stop")
    if "\t" in text:
        raise ValueError("fortune must not contain a tab")
    if not text.isascii():
        raise ValueError("fortune must be plain ASCII")
    if not text[0].isupper():
        raise ValueError("fortune must start with a capital letter")
    # The line must agree with the clauses it was built from:
    # rebuild it here from the raw word groups and check that the
    # word count and the clause boundaries still line up, so a
    # stray edit to one group cannot silently change the entry.
    words = text.split(" ")
    expected_words = len(OPENING_WORDS) + len(EARNING_WORDS) + len(ESCAPE_WORDS)
    if len(words) != expected_words:
        raise ValueError(
            f"fortune must have {expected_words} words, got {len(words)}"
        )
    if tuple(words[: len(OPENING_WORDS)]) != OPENING_WORDS:
        raise ValueError("fortune opening clause does not match its parts")
    if tuple(words[len(OPENING_WORDS) : len(OPENING_WORDS) + len(EARNING_WORDS)]) != EARNING_WORDS:
        raise ValueError("fortune earning clause does not match its parts")
    if tuple(words[-len(ESCAPE_WORDS) :]) != ESCAPE_WORDS:
        raise ValueError("fortune closing clause does not match its parts")
    if "midnight" not in words or "on-call" not in words:
        raise ValueError("fortune must keep its midnight and on-call turns")
    encoded = text.encode("utf-8")
    if encoded.decode("utf-8") != text:
        raise ValueError("fortune must survive a UTF-8 round trip")
    if len(encoded) != len(text):
        raise ValueError("fortune must encode to one byte per character")


def main() -> int:
    fortune = assemble_fortune()
    validate_fortune(fortune)

    payload = fortune.encode("utf-8")
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "wb") as fh:
        fh.write(payload)

    with open(OUTPUT_PATH, "rb") as fh:
        written = fh.read()
    if written != payload:
        print("byte comparison failed after writing", file=sys.stderr)
        return 1
    if written.decode("utf-8") != fortune:
        print("round-trip text mismatch after writing", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
