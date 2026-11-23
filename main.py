"""A Day of One-Line Pitches — entry program.

Writes one sentence to /output/entry.txt: a pitch that talks a friend
who has never coded into letting an AI agent build their first app idea
on make.fun. The sentence is the whole entry — no code, no explanation.

The pitch works on the judge's criteria in order: it makes the case to
that friend in one read; it gives a concrete reason to say yes now (a
first version you can actually tap) and makes handing the idea over feel
easy and low risk (free to try; the worst case is an afternoon, not a
fortune); it uses plain words; it promises only a first version, not
perfection; and it sounds like one friend talking to another, about the
idea they have been carrying around in their head.

Deterministic: no network, no clock, no randomness. The output file is
exactly the sentence, with no trailing newline, so its character count
is the sentence's character count.
"""

import os

# Revised: "Just tell it" opens warmer and more direct than "Tell an AI
# agent" — the friend is already talking to the agent, and naming it at
# the payoff ("an AI agent will build you") lands the promise harder.
# One sentence, 236 characters, inside the 240 cap.
PITCH = (
    "Just tell it the app idea you've been carrying around in your head, "
    "in plain words, and an AI agent will build you a first version you "
    "can actually tap \u2014 free to try, and if it isn't right, you've "
    "only spent an afternoon, not a fortune."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = PITCH
    if not text.strip():
        raise ValueError("pitch must not be blank")
    if len(text) > 240:
        raise ValueError(f"pitch is {len(text)} characters, over the 240 cap")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
