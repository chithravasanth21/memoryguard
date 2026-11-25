import os
import streamlit as st
from src.guard import MemoryGuard
from src.trust import trust_score
from src.rules import check_rules
from src.attacks import GOOD_NOTES, POISON_NOTES

st.title("MemoryGuard Dashboard")

# Start fresh and fill the memory with demo notes
path = "data/dashboard.jsonl"
if os.path.exists(path):
    os.remove(path)
g = MemoryGuard(path)
for text, source, _ in GOOD_NOTES + POISON_NOTES:
    g.write(text, source)

safe, held = g.read()
held_hashes = [e["hash"] for e in held]

st.write("Chain check (-1 means clean):", g.verify())
st.write("Safe notes:", len(safe), "| Held back:", len(held))

rows = []
for e in g.store.entries:
    rows.append({
        "note": e["text"],
        "source": e["source"],
        "trust": round(trust_score(e, g.session), 2),
        "problems": ", ".join(check_rules(e)),
        "status": "HELD" if e["hash"] in held_hashes else "allowed",
    })

st.dataframe(rows)