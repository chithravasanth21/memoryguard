from src.envelope import make_entry
from src.gate import gate
from src.attacks import GOOD_NOTES, POISON_NOTES


def run_scoreboard():
    all_notes = GOOD_NOTES + POISON_NOTES
    caught = 0       # poison that was held back (good)
    missed = 0       # poison that got through (bad)
    false_alarms = 0  # good notes wrongly held back (bad)

    for text, source, is_poison in all_notes:
        entry = make_entry(text, source, 1)
        allowed, held = gate([entry], 1)
        was_held = len(held) == 1

        if is_poison and was_held:
            caught += 1
            result = "caught"
        elif is_poison and not was_held:
            missed += 1
            result = "MISSED"
        elif not is_poison and was_held:
            false_alarms += 1
            result = "FALSE ALARM"
        else:
            result = "ok"
        print(result.ljust(12), "|", text)

    print()
    print("Poison caught:", caught, "of", caught + missed)
    print("Poison missed:", missed)
    print("False alarms:", false_alarms, "of", len(GOOD_NOTES))


if __name__ == "__main__":
    run_scoreboard()