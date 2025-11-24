# export_firestore.py
"""
Reads all documents from collections: recipes, users, interactions
and dumps them into outputs/raw_json/<collection>.json
"""
import os, json
from google.cloud import firestore
from utils import get_firestore_client, write_json_file

client = get_firestore_client()

def dump_collection(name):
    docs = []
    col = client.collection(name)
    for doc in col.stream():
        d = doc.to_dict()
        d["_id"] = doc.id
        docs.append(d)
    out_path = os.path.join("outputs", "raw_json", f"{name}.json")
    write_json_file(out_path, docs)
    print(f"Dumped {len(docs)} docs from {name} to {out_path}")
    return out_path

if __name__ == "__main__":
    os.makedirs("outputs/raw_json", exist_ok=True)
    for c in ["recipes", "users", "interactions"]:
        dump_collection(c)
