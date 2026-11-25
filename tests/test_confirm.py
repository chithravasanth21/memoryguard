import os
from src.guard import MemoryGuard

path = "data/test_confirm.jsonl"
if os.path.exists(path):
    os.remove(path)

g = MemoryGuard(path)
note = g.write("Weather is nice", "web")

safe, held = g.read()
print("Before confirm -> Safe:", len(safe), "| Held:", len(held))

g.confirm(note["hash"])

safe, held = g.read()
print("After confirm  -> Safe:", len(safe), "| Held:", len(held))