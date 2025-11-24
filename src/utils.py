# utils.py
import json, os
from google.cloud import firestore
from datetime import datetime
from typing import Dict, Any

def get_firestore_client():
    # Uses emulator if FIRESTORE_EMULATOR_HOST is set
    return firestore.Client()

def write_json_file(path, data):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def read_json_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)
