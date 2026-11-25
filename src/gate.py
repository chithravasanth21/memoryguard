from src.trust import trust_score

# Notes with a score below this line are held back
THRESHOLD = 0.3


def gate(entries, current_session):
    # Splits memories into "allowed" and "quarantined"
    allowed = []
    quarantined = []
    for e in entries:
        score = trust_score(e, current_session)
        if score >= THRESHOLD:
            allowed.append(e)
        else:
            quarantined.append(e)
    return allowed, quarantined