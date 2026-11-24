"""make.fun bounty: Dad Joke Showdown.

Deterministic, no-network program. Writes exactly one dad joke to
/output/entry.txt. The joke is the kind a real dad says at the
breakfast table: simple, corny, one pun, straight face. Running
twice writes identical bytes.
"""
from pathlib import Path

JOKE = "I put my savings in the blender. Now my money is liquid."

OUT = Path("/output/entry.txt")


def main() -> None:
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(JOKE, encoding="utf-8")
    print(f"Wrote {OUT} ({len(JOKE)} chars)")


if __name__ == "__main__":
    main()
