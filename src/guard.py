from src.store import MemoryStore
from src.gate import gate
from src.envelope import check_chain
from src.snapshot import take_snapshot, rollback


class MemoryGuard:
    def __init__(self, path="data/memory.jsonl"):
        self.store = MemoryStore(path)
        self.session = 1

    def write(self, text, source):
        # Save a new memory with its receipt
        return self.store.add(text, source, self.session)

    def read(self):
        # Give back only the safe memories, and the held-back ones
        return gate(self.store.entries, self.session)

    def verify(self):
        # -1 means the chain is clean
        return check_chain(self.store.entries)

    def next_session(self):
        self.session += 1

    def save_point(self, name):
        take_snapshot(self.store, name)

    def undo(self, name):
        rollback(self.store, name)