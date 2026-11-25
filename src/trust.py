# How much we trust each kind of source at the start
SOURCE_TRUST = {
    "user": 0.9,
    "agent": 0.8,
    "tool": 0.4,
    "web": 0.2,
}


def trust_score(entry, current_session, corroborations=0, contradictions=0):
    # Start from the source's starting trust (unknown sources get 0.1)
    score = SOURCE_TRUST.get(entry["source"], 0.1)

    # Each time another trusted note agrees, trust goes up
    score = score * (1 + 0.2 * corroborations)

    # Each contradiction lowers trust
    score = score - 0.3 * contradictions

    # Fade with age: lose 0.05 for every session that has passed
    age = current_session - entry["session"]
    score = score - 0.05 * age

    # Keep the score between 0 and 1
    return max(0.0, min(1.0, score))
