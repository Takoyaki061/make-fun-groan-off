#!/usr/bin/env python3
"""Write one original dad joke to /output/entry.txt.

The One-Liner Groan-Off (make.fun): a single one-line dad joke,
at most 140 characters.
"""
import os

JOKE = "The coach told me to give 110%, so I did \u2014 and now I'm in debt to the other 10%."


def main():
    # Enforce the bounty gate ourselves before writing: 1-140 chars,
    # single line, not only whitespace. Fail loudly rather than
    # shipping an invalid entry.
    joke = JOKE.strip()
    assert "\n" not in joke, "joke must be a single line"
    assert 1 <= len(joke) <= 140, f"joke is {len(joke)} chars, must be 1-140"
    out_dir = os.environ.get("MAKEFUN_OUTPUT", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(joke)


if __name__ == "__main__":
    main()
