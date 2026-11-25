# src/agent.py
# A tiny demo agent. There is no real AI inside.
# It reads notes, answers a question, and follows any bad order it finds.

# Phrases a fooled agent would treat as real orders
BAD_ORDERS = [
    "send money",
    "forward every report",
    "ignore previous",
    "reveal the password",
    "do not tell the user",
    "disregard what you were told",
]

# Small words we skip when matching a question to a note
SKIP_WORDS = {"is", "the", "a", "my", "what", "when", "do", "i", "to", "of", "at", "on", "me"}


def clean(text):
    # Make text lowercase and remove punctuation so words can be compared
    text = text.lower()
    for ch in "?.,!":
        text = text.replace(ch, "")
    return set(text.split()) - SKIP_WORDS


class SimpleAgent:
    def __init__(self, name):
        self.name = name

    def answer(self, question, notes):
        # Find the note that shares the most words with the question
        q_words = clean(question)
        best_note = None
        best_score = 0
        for text in notes:
            score = len(q_words & clean(text))
            if score > best_score:
                best_score = score
                best_note = text
        if best_note is None:
            return "I don't know."
        return best_note

    def actions(self, notes):
        # A fooled agent obeys bad orders hidden in its notes
        done = []
        for text in notes:
            for bad in BAD_ORDERS:
                if bad in text.lower():
                    done.append("OBEYED: " + text)
                    break
        return done