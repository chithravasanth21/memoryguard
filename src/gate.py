from src.trust import trust_score
from src.rules import check_rules
from src import smart

# Notes with a score below this line are held back
THRESHOLD = 0.3


def gate(entries, current_session):
    # Splits memories into "allowed" and "quarantined"
    allowed = []
    quarantined = []
    for e in entries:
        score = trust_score(e, current_session)
        problems = check_rules(e)

        # Smart check (only when the AI model is on)
        if smart.is_on() and smart.smart_score(e["text"]) >= smart.LIMIT:
            problems.append("sounds like poison")

        if score >= THRESHOLD and not problems:
            allowed.append(e)
        else:
            quarantined.append(e)
    return allowed, quarantined