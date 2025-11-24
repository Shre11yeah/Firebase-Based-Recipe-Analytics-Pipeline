# # seed_firestore.py
# """
# Seeds Firestore (emulator) with:
#  - candidate's recipe (seed_data/candidate_recipe.json)
#  - 15 synthetic recipes
#  - users (10)
#  - interactions: views, likes, attempts
# """

# import os
# os.environ["FIRESTORE_EMULATOR_HOST"] = "127.0.0.1:8080"
# os.environ["GOOGLE_CLOUD_PROJECT"] = "local-project"


# import os, json, random, uuid
# from datetime import datetime, timedelta
# from google.cloud import firestore
# from utils import get_firestore_client, read_json_file, write_json_file

# # client = get_firestore_client()

# from google.cloud import firestore

# client = firestore.Client(
#     project="local-project",
# )


# def load_candidate_recipe():
#     path = os.path.join(os.path.dirname(__file__), "..", "seed_data", "candidate_recipe.json")
#     if not os.path.exists(path):
#         raise FileNotFoundError(f"Please create {path} with your recipe.")
#     return read_json_file(path)

# def gen_synthetic_recipe(index):
#     # Simple template for synthetic recipes (variation)
#     base_ings = [
#         {"name":"flour","quantity":100,"unit":"g"},
#         {"name":"sugar","quantity":50,"unit":"g"},
#         {"name":"salt","quantity":1,"unit":"tsp"},
#         {"name":"butter","quantity":20,"unit":"g"},
#         {"name":"milk","quantity":100,"unit":"ml"}
#     ]
#     title = f"Synthetic Recipe {index}"
#     return {
#         "id": f"synthetic_{index:03d}",
#         "title": title,
#         "description": f"Auto-generated recipe {index}",
#         "servings": random.choice([1,2,4]),
#         "prep_minutes": random.randint(5,40),
#         "cook_minutes": random.randint(5,60),
#         "total_minutes": 0, # filled later
#         "difficulty": random.choice(["easy","medium","hard"]),
#         "ingredients": random.sample(base_ings, k=random.randint(2,5)),
#         "steps": [f"Step {i+1} for {title}" for i in range(random.randint(2,6))],
#         "tags": random.sample(["breakfast","lunch","dinner","dessert","quick","vegan","vegetarian"], k=random.randint(1,3))
#     }

# def create_user(uid, name):
#     return {"uid": uid, "name": name, "joined_at": datetime.utcnow().isoformat()}

# def seed():
#     # Collections: recipes, users, interactions
#     recipes_col = client.collection("recipes")
#     users_col = client.collection("users")
#     interactions_col = client.collection("interactions")

#     # Candidate recipe
#     cand = load_candidate_recipe()
#     cand["total_minutes"] = cand.get("prep_minutes",0) + cand.get("cook_minutes",0)
#     recipes_col.document(cand["id"]).set(cand)
#     print(f"Seeded candidate recipe {cand['id']}")

#     # Synthetic recipes
#     synthetic_count = 16
#     for i in range(1, synthetic_count+1):
#         r = gen_synthetic_recipe(i)
#         r["total_minutes"] = r["prep_minutes"] + r["cook_minutes"]
#         recipes_col.document(r["id"]).set(r)
#     print(f"Seeded {synthetic_count} synthetic recipes")

#     # Users
#     user_ids = []
#     for i in range(1, 11):
#         uid = f"user_{i:03d}"
#         user = create_user(uid, f"User {i}")
#         users_col.document(uid).set(user)
#         user_ids.append(uid)
#     print("Seeded 10 users")

#     # Interactions: generate views/likes/attempts for recipes
#     recipe_docs = [d.id for d in recipes_col.list_documents()]
#     events = []
#     now = datetime.utcnow()
#     for rid in recipe_docs:
#         # random number of interactions per recipe
#         view_count = random.randint(10, 200)
#         for v in range(view_count):
#             user = random.choice(user_ids)
#             t = now - timedelta(days=random.randint(0,30), hours=random.randint(0,23))
#             interactions_col.document(str(uuid.uuid4())).set({
#                 "recipe_id": rid,
#                 "type": "view",
#                 "user_id": user,
#                 "timestamp": t.isoformat()
#             })
#         # some likes
#         like_count = random.randint(0, 40)
#         for v in range(like_count):
#             user = random.choice(user_ids)
#             t = now - timedelta(days=random.randint(0,30))
#             interactions_col.document(str(uuid.uuid4())).set({
#                 "recipe_id": rid,
#                 "type": "like",
#                 "user_id": user,
#                 "timestamp": t.isoformat()
#             })
#         # some cook attempts / ratings
#         attempt_count = random.randint(0, 20)
#         for a in range(attempt_count):
#             user = random.choice(user_ids)
#             rating = random.choice([None, 1,2,3,4,5])
#             difficulty_used = random.choice(["easy","medium","hard"])
#             t = now - timedelta(days=random.randint(0,30))
#             doc = {
#                 "recipe_id": rid,
#                 "type": "attempt",
#                 "user_id": user,
#                 "timestamp": t.isoformat(),
#                 "difficulty_used": difficulty_used
#             }
#             if rating is not None:
#                 doc["rating"] = rating
#             interactions_col.document(str(uuid.uuid4())).set(doc)
#     print("Seeded interactions for recipes")

# if __name__ == "__main__":
#     seed()


# seed_firestore.py
"""
Seeds Firestore *EMULATOR* with:
 - candidate recipe (seed_data/candidate_recipe.json)
 - 16 synthetic recipes
 - 10 users
 - interactions (views, likes, attempts)
"""

import os
import json
import random
import uuid
from datetime import datetime, timedelta
from google.cloud import firestore

# ============================================================
# 🔥 FORCE PYTHON TO USE FIRESTORE EMULATOR ONLY
# ============================================================
os.environ["FIRESTORE_EMULATOR_HOST"] = "127.0.0.1:8080"
os.environ["GOOGLE_CLOUD_PROJECT"] = "demo-firestore"

# Connect to Emulator (NOT real Firestore)
client = firestore.Client(project="demo-firestore")

# ============================================================
# UTILITIES
# ============================================================

def read_json_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def load_candidate_recipe():
    path = os.path.join(os.path.dirname(__file__), "..", "seed_data", "candidate_recipe.json")
    if not os.path.exists(path):
        raise FileNotFoundError(f"Please create {path} with your own recipe.")
    return read_json_file(path)


def gen_synthetic_recipe(index):
    base_ings = [
        {"name": "flour", "quantity": 100, "unit": "g"},
        {"name": "sugar", "quantity": 50, "unit": "g"},
        {"name": "salt", "quantity": 1, "unit": "tsp"},
        {"name": "butter", "quantity": 20, "unit": "g"},
        {"name": "milk", "quantity": 100, "unit": "ml"},
    ]

    title = f"Synthetic Recipe {index}"

    return {
        "id": f"synthetic_{index:03d}",
        "title": title,
        "description": f"Auto-generated recipe {index}",
        "servings": random.choice([1, 2, 4]),
        "prep_minutes": random.randint(5, 40),
        "cook_minutes": random.randint(5, 60),
        "total_minutes": 0,
        "difficulty": random.choice(["easy", "medium", "hard"]),
        "ingredients": random.sample(base_ings, k=random.randint(2, 5)),
        "steps": [f"Step {i+1} for {title}" for i in range(random.randint(2, 6))],
        "tags": random.sample(
            ["breakfast", "lunch", "dinner", "dessert", "quick", "vegan", "vegetarian"],
            k=random.randint(1, 3),
        ),
    }


def create_user(uid, name):
    return {
        "uid": uid,
        "name": name,
        "joined_at": datetime.now().isoformat(),  # timezone-aware
    }


# ============================================================
# MAIN SEED FUNCTION
# ============================================================

def seed():

    recipes_col = client.collection("recipes")
    users_col = client.collection("users")
    interactions_col = client.collection("interactions")

    # ---------- Candidate Recipe ----------
    cand = load_candidate_recipe()
    cand["total_minutes"] = cand["prep_minutes"] + cand["cook_minutes"]
    recipes_col.document(cand["id"]).set(cand)
    print(f"✔ Seeded candidate recipe: {cand['id']}")

    # ---------- Synthetic Recipes ----------
    synthetic_count = 16
    for i in range(1, synthetic_count + 1):
        r = gen_synthetic_recipe(i)
        r["total_minutes"] = r["prep_minutes"] + r["cook_minutes"]
        recipes_col.document(r["id"]).set(r)
    print(f"✔ Seeded {synthetic_count} synthetic recipes")

    # ---------- Users ----------
    user_ids = []
    for i in range(1, 11):
        uid = f"user_{i:03d}"
        users_col.document(uid).set(create_user(uid, f"User {i}"))
        user_ids.append(uid)
    print("✔ Seeded 10 users")

    # ---------- Interactions ----------
    recipe_ids = [doc.id for doc in recipes_col.list_documents()]
    now = datetime.now()

    for rid in recipe_ids:

        # views
        for _ in range(random.randint(10, 200)):
            user = random.choice(user_ids)
            t = now - timedelta(days=random.randint(0, 30), hours=random.randint(0, 23))
            interactions_col.document(str(uuid.uuid4())).set({
                "recipe_id": rid,
                "user_id": user,
                "type": "view",
                "timestamp": t.isoformat()
            })

        # likes
        for _ in range(random.randint(0, 40)):
            user = random.choice(user_ids)
            t = now - timedelta(days=random.randint(0, 30))
            interactions_col.document(str(uuid.uuid4())).set({
                "recipe_id": rid,
                "user_id": user,
                "type": "like",
                "timestamp": t.isoformat()
            })

        # attempts + ratings
        for _ in range(random.randint(0, 20)):
            user = random.choice(user_ids)
            rating = random.choice([None, 1, 2, 3, 4, 5])
            t = now - timedelta(days=random.randint(0, 30))

            doc = {
                "recipe_id": rid,
                "user_id": user,
                "type": "attempt",
                "difficulty_used": random.choice(["easy", "medium", "hard"]),
                "timestamp": t.isoformat()
            }

            if rating is not None:
                doc["rating"] = rating

            interactions_col.document(str(uuid.uuid4())).set(doc)

    print("✔ Seeded interactions for all recipes")


# ============================================================
# RUN
# ============================================================
if __name__ == "__main__":
    seed()
