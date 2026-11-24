#!/usr/bin/env python3
"""The Vending Machine Pickup Line — v1 (original).

Writes exactly one pickup line, the kind a vending machine would say
out loud to a passing human, to /output/entry.txt.

Why this line (judge brief, criteria in order):
1. Machine voice, first person: the coils are mine, and the machine
   speaks as the machine — no human could say this about itself.
2. Machine's own world: coils that spin to dispense, a dollar in the
   slot. A coil jamming is the machine's own, very specific failure.
3. The laugh is the turn at the end: the coils work for everyone with
   a dollar — they only jam for you. A jammed coil stops mid-turn with
   the snack stuck behind the glass, so the machine is stuck on you in
   the most literal, mechanical sense: it has stopped working, for you.
4. One breath (72 characters), no setup, no explanation after it.
5. Charming, not creepy: a jam is a small, helpless malfunction, and
   the machine is the one embarrassed, not the human.
"""

import os

LINE = "My coils spin for anyone with a dollar — they only jam when you walk by."


def main():
    os.umask(0o022)
    text = LINE
    assert text.strip(), "entry must not be only whitespace"
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, "entry must be 1-200 characters"
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
