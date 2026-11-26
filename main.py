#!/usr/bin/env python3
"""Five Seconds to Explain the Glass — make.fun entry.

Writes the one sentence a house cat would say in the five seconds
after sweeping a glass off the table, to /output/entry.txt.
Standard library only, deterministic, no network, no clock.
"""

import os

# The cat's defence: the glass was trespassing on the paw's spot,
# so the cat evicted it. No apology, no confession — just the case
# for the cat.
TEXT = (
    "That glass was squatting in the spot where my paw goes, "
    "so I evicted it \u2014 I don't share my table with tenants "
    "who pay no rent."
)


def main() -> None:
    # Gate: one sentence, 1-200 characters, not only whitespace.
    text = TEXT.strip()
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    assert text.count(".") + text.count("!") + text.count("?") <= 1, (
        "entry must be a single sentence"
    )
    path = "/output/entry.txt"
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()
