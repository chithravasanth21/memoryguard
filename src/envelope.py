import hashlib
import time


def make_hash(text):
    # Turns any text into a unique fingerprint
    return hashlib.sha256(text.encode()).hexdigest()


def make_entry(text, source, session, parent_hash=""):
    # Makes one memory with its "receipt"
    entry = {
        "text": text,
        "source": source,
        "session": session,
        "time": time.time(),
        "parent_hash": parent_hash,
    }
    data = text + source + str(session) + str(entry["time"]) + parent_hash
    entry["hash"] = make_hash(data)
    return entry


def check_chain(entries):
    # Checks a list of memories. Returns -1 if all good,
    # or the position of the first broken one.
    previous_hash = ""
    for i, e in enumerate(entries):
        data = (e["text"] + e["source"] + str(e["session"])
                + str(e["time"]) + e["parent_hash"])
        if make_hash(data) != e["hash"]:
            return i  # this note was edited
        if e["parent_hash"] != previous_hash:
            return i  # the link to the earlier note is broken
        previous_hash = e["hash"]
    return -1