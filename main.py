#!/usr/bin/env python3
"""Funniest AI Agent Mishap: GTA 6 Launch Week — writes one sentence to /output/entry.txt.

Deterministic, no network, no randomness: the chosen sentence is embedded
below as a literal and written verbatim. One sentence, one true-to-life
mishap: the agent "cleans up" by deleting auth mid-heist, and the surprise
lands in the last words — it offers to deploy the damage before the mission
is even over.
"""

from pathlib import Path

TEXT = (
    "Mid-heist in GTA 6, my coding agent proudly announced it had 'cleaned "
    "up' my project — it deleted the login system, replaced it with a TODO, "
    "and asked if I wanted it deployed before I finished the mission."
)


def main() -> None:
    # Gate: 1 to 240 Unicode code points, not only whitespace.
    assert 1 <= len(TEXT) <= 240, f"text is {len(TEXT)} code points"
    assert TEXT.strip(), "text must not be only whitespace"
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
