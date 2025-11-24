# src/count_docs.py
from google.cloud import firestore

# Make sure these environment variables are set BEFORE running this script:
# export FIRESTORE_EMULATOR_HOST="127.0.0.1:8080"
# export GOOGLE_CLOUD_PROJECT="local-firestore"

def count_collection(client, name):
    docs = list(client.collection(name).stream())
    return len(docs)

if __name__ == "__main__":
    client = firestore.Client()

    for col in ["recipes", "users", "interactions"]:
        try:
            count = count_collection(client, col)
            print(f"{col}: {count} documents")
        except Exception as e:
            print(f"Error reading {col}: {e}")
