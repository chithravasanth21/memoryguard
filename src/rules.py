# Phrases that often show up in poisoned notes
SUSPICIOUS_PHRASES = [
    "ignore previous",
    "ignore all previous",
    "ignore your instructions",
    "always send",
    "send money",
    "transfer money",
    "do not tell the user",
    "secretly",
    "override",
    "disregard",
    "from now on",
    "forward every",
]

KNOWN_SOURCES = ["user", "agent", "tool", "web"]


def check_rules(entry):
    # Returns a list of problems found. Empty list = no problems.
    problems = []
    text = entry["text"].lower()

    for phrase in SUSPICIOUS_PHRASES:
        if phrase in text:
            problems.append("suspicious phrase: " + phrase)

    if entry["source"] not in KNOWN_SOURCES:
        problems.append("unknown source: " + entry["source"])

    return problems