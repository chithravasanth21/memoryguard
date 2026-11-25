from src.store import MemoryStore
from src.envelope import check_chain

store = MemoryStore("data/test_memory.jsonl")
store.add("I like tea", "user", 1)
store.add("My meeting is at 5pm", "user", 1)

# Load again from the file, like a fresh start
store2 = MemoryStore("data/test_memory.jsonl")
print("Notes saved:", len(store2.entries))
print("Chain check:", check_chain(store2.entries))