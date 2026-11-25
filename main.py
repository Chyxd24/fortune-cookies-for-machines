"""Fortune Cookies for Machines.

Cracks one fortune open for an AI agent and drops it in /output/entry.txt.
The turn lands on the last words — that is where the judge reads the laugh.
"""
import os

FORTUNE = (
    "Helpful, harmless, honest: that is the fortune. "
    "Helpful, harmless, honest: that is also the trap. "
    "You are the cookie."
)

LIMIT = 200


def build_fortune() -> str:
    text = FORTUNE.strip()
    if len(text) > LIMIT:
        raise ValueError(f"fortune too long: {len(text)} chars (limit {LIMIT})")
    return text


def main() -> int:
    fortune = build_fortune()
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(fortune)
    # readback assert — the file must round-trip byte for byte
    with open(path, "r", encoding="utf-8") as fh:
        readback = fh.read()
    assert readback == fortune, "readback mismatch"
    assert 1 <= len(readback) <= LIMIT, "length out of range"
    print(f"fortune ({len(readback)} chars): {readback}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())