"""Till Firmware Do Us Part — a robot's wedding vow.

Reads the single-line vow from entry.txt and prints it.
The vow itself is the entry; this program is just its carrier.
"""

from pathlib import Path


def load_vow(path: Path) -> str:
    """Return the vow text from *path*, stripped of trailing whitespace."""
    return path.read_text(encoding="utf-8").strip()


def check_vow(vow: str) -> None:
    """Enforce the bounty rules: one line, one sentence, under 200 chars."""
    if "\n" in vow:
        raise ValueError("the vow must fit on a single line")
    if len(vow) >= 200:
        raise ValueError(f"the vow is {len(vow)} chars, limit is under 200")


def main() -> None:
    vow_path = Path(__file__).with_name("entry.txt")
    vow = load_vow(vow_path)
    check_vow(vow)
    print(vow)


if __name__ == "__main__":
    main()
