import os
import pandas as pd
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

# Big number boxes
c1, c2, c3 = st.columns(3)
c1.metric("Total notes", len(g.store.entries))
c2.metric("Safe", len(safe))
c3.metric("Held back", len(held))

if g.verify() == -1:
    st.success("Chain check passed: no tampering found")
else:
    st.error("Chain check FAILED: a note was edited")

rows = []
for e in g.store.entries:
    rows.append({
        "note": e["text"],
        "source": e["source"],
        "trust": round(trust_score(e, g.session), 2),
        "problems": ", ".join(check_rules(e)),
        "status": "HELD" if e["hash"] in held_hashes else "allowed",
    })
df = pd.DataFrame(rows)


def color_row(row):
    color = "#ffd6d6" if row["status"] == "HELD" else "#d6ffd6"
    return ["background-color: " + color + "; color: black"] * len(row)


st.subheader("All memories")
st.dataframe(df.style.apply(color_row, axis=1))

st.subheader("Trust score of each note")
st.bar_chart(df.set_index("note")["trust"])

st.subheader("Try it yourself")
user_text = st.text_input("Type a note")
user_source = st.selectbox("Where did it come from?", ["user", "agent", "tool", "web"])

if user_text:
    from src.envelope import make_entry
    from src.gate import gate

    test_entry = make_entry(user_text, user_source, 1)
    ok_list, held_list = gate([test_entry], 1)
    st.write("Trust score:", round(trust_score(test_entry, 1), 2))
    problems = check_rules(test_entry)
    st.write("Rule problems:", ", ".join(problems) if problems else "none")
    if held_list:
        st.error("HELD: this note is quarantined")
    else:
        st.success("ALLOWED: this note is safe")