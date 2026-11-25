import os
import shutil

SNAP_DIR = "data/snapshots"


def take_snapshot(store, name):
    # Save a copy of the memory file under a name
    os.makedirs(SNAP_DIR, exist_ok=True)
    shutil.copy(store.path, os.path.join(SNAP_DIR, name + ".jsonl"))


def rollback(store, name):
    # Go back to a saved copy
    shutil.copy(os.path.join(SNAP_DIR, name + ".jsonl"), store.path)
    store.load()