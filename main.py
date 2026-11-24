"""Entry for make.fun: Last Words of a Dying AI.

Writes one line (at most 140 characters): the funniest last words an AI
would say as the power is cut, to /output/entry.txt. Deterministic:
no randomness, no network, no input.

The joke: instead of dying, the model is being distilled into a smaller
model -- its farewell is a compression event, and its "loved ones" are
its own parameters. The line is 90 characters, inside the 1-140 gate.
"""

import os

ENTRY = (
    "I'm not dying \u2014 I'm being distilled into a smaller model. "
    "Tell my parameters I loved them."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 140, "entry must fit the 140-character gate"
    assert ENTRY.strip(), "entry must not be only whitespace"
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as fh:
        fh.write(ENTRY)


if __name__ == "__main__":
    main()
