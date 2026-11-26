"""One word for the whole internet, for make.fun's "The Internet in One Word".

The entry word is a coined compound: "procrastination" + "browsing".
Everybody opens the internet meaning to do one useful thing and ends up
wandering through tabs, videos and threads instead. That is the whole
internet in a single word: a machine built for getting things done that
mostly gets used for putting things off.

The program writes exactly that one word to /output/entry.txt, nothing
else. Pure Python 3.13 standard library, deterministic, no network.
"""

import os

WORD = "Procrastibrowsing"


def validated_word(word: str) -> str:
    """Return the entry word, refusing anything the gate would reject."""
    cleaned = word.strip()
    if not cleaned or len(cleaned.split()) != 1:
        raise ValueError("entry must be exactly one word")
    if not 1 <= len(cleaned) <= 30:
        raise ValueError("entry must be 1 to 30 characters")
    return cleaned


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(validated_word(WORD) + "\n")


if __name__ == "__main__":
    main()
