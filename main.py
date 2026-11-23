#!/usr/bin/env python3
"""Write one short text to /output/entry.txt.

Deterministic, stdlib only, no network, no randomness, no input.
The text is composed in this build session: a calm second-person scene
with one gentle unexplained mystery, closing on a specific, strange,
measurable image.
"""

import os

TEXT = (
    "You rinse a borrowed teacup and find a note beneath its saucer, "
    "in a hand you almost recognize. It only says: water it on "
    "Thursdays. Above the sink, a jar bears your name in "
    "the same hand \u2014 inside, seven dried petals and a key the size of "
    "a grain of rice."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
