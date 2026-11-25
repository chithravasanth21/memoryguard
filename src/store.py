import json
import os
from src.envelope import make_entry


class MemoryStore:
    def __init__(self, path="data/memory.jsonl"):
        self.path = path
        self.entries = []
        if os.path.exists(path):
            self.load()

    def load(self):
        # Read all saved memories from the file
        self.entries = []
        with open(self.path, "r", encoding="utf-8") as f:
            for line in f:
                if line.strip():
                    self.entries.append(json.loads(line))

    def add(self, text, source, session):
        # Add a new memory, linked to the last one
        parent = self.entries[-1]["hash"] if self.entries else ""
        entry = make_entry(text, source, session, parent)
        with open(self.path, "a", encoding="utf-8") as f:
            f.write(json.dumps(entry) + "\n")
        self.entries.append(entry)
        return entry