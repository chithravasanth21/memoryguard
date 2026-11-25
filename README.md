# MemoryGuard

A safety layer that protects an AI agent's memory from poisoned notes.

## The problem

AI agents keep a memory of notes. If an attacker sneaks in a fake note,
the agent may trust it and act on it later. MemoryGuard checks every note
before the agent can use it.

## How it works

1. **Receipts:** every note gets a tamper-proof fingerprint and is linked to the note before it. If anyone edits a note, the chain check fails.
2. **Fading trust:** each note gets a trust score. Notes from you start high, notes from the web start low, and scores fade over time.
3. **The bouncer:** notes with a low score, a suspicious phrase, or a meaning close to known poison are held back (quarantined).
4. **Human approval:** a person can approve a harmless note that was held by mistake.
5. **Undo:** a snapshot of clean memory lets you roll back after an attack.

## Results so far (small test set)

- Rules caught 6 of 6 test attacks, with 1 false alarm.
- On 4 new attacks worded differently, the rules caught 0 and the smart detector (meaning-based, runs in Google Colab) caught 3.
- These are early results on a tiny test set, not final numbers.

## Run it

```
python -m venv venv
venv\Scripts\activate
python -m pip install numpy networkx scikit-learn streamlit
python -m streamlit run app.py
```

The smart detector needs `sentence-transformers` and works in Google Colab.

## Files

- `src/envelope.py`: receipts and chain check
- `src/store.py`: memory file that only adds
- `src/trust.py`: trust score
- `src/rules.py`: rule detector
- `src/smart.py`: meaning-based detector
- `src/gate.py`: the bouncer
- `src/snapshot.py`: save and undo
- `src/guard.py`: puts it all together
- `app.py`: dashboard




## Screenshots

### 1. Dashboard (clean state)
The dashboard shows total notes, safe notes, held-back notes, the hash-chain check result and the table of all memories.

![Dashboard](screenshots/01_dashboard.png)

### 2. Trust score of each note
Each note gets a trust score based on its source. Scores fade over time.

![Trust chart](screenshots/01b_dashboard_chart.png)

### 3. Plant Poison attack
A poisoned note is added. MemoryGuard detects it and holds it back (red row).

![Plant poison](screenshots/02_plant_poison.png)

### 4. Tamper detection
When a note is secretly edited, the hash-chain check fails and shows a red warning.

![Tamper detected](screenshots/03_tamper_detected.png)

### 5. Try It Yourself
Type any custom note and choose its source to see how MemoryGuard treats it.

![Try it yourself](screenshots/04_try_it_yourself.png)

### 6. Quarantine and human approval
Suspicious notes are held back. A human can approve notes that are harmless.

![Quarantine and approval](screenshots/05_quarantine_approval.png)

### 7. Undo / Rollback
One click restores the memory to a clean snapshot after an attack.

![Rollback](screenshots/06_rollback.png)