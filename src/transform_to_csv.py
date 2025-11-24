# transform_to_csv.py
"""
Transforms outputs/raw_json/*.json into normalized CSVs:
 - outputs/csv/recipe.csv
 - outputs/csv/ingredients.csv
 - outputs/csv/steps.csv
 - outputs/csv/interactions.csv
"""

import os, csv, json, uuid
from utils import read_json_file, write_json_file

CSV_DIR = os.path.join("outputs","csv")
os.makedirs(CSV_DIR, exist_ok=True)

def normalize_recipes(recipes_json_path):
    recipes = read_json_file(recipes_json_path)
    recipes_rows = []
    ingredients_rows = []
    steps_rows = []
    for r in recipes:
        r_id = r.get("id") or r.get("_id") or str(uuid.uuid4())
        recipes_rows.append({
            "recipe_id": r_id,
            "title": r.get("title"),
            "description": r.get("description"),
            "servings": r.get("servings"),
            "prep_minutes": r.get("prep_minutes"),
            "cook_minutes": r.get("cook_minutes"),
            "total_minutes": r.get("total_minutes"),
            "difficulty": r.get("difficulty"),
            "tags": "|".join(r.get("tags", []))
        })
        for idx, ing in enumerate(r.get("ingredients", [])):
            ingredients_rows.append({
                "ingredient_id": f"{r_id}_ing_{idx+1}",
                "recipe_id": r_id,
                "name": ing.get("name"),
                "quantity": ing.get("quantity"),
                "unit": ing.get("unit"),
                "notes": ing.get("notes", "")
            })
        for idx, step in enumerate(r.get("steps", [])):
            steps_rows.append({
                "step_id": f"{r_id}_step_{idx+1}",
                "recipe_id": r_id,
                "step_number": idx+1,
                "instruction": step
            })
    # write CSVs
    def write_csv(path, rows, headers):
        with open(path, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            for row in rows:
                writer.writerow(row)
    write_csv(os.path.join(CSV_DIR,"recipe.csv"), recipes_rows,
              ["recipe_id","title","description","servings","prep_minutes","cook_minutes","total_minutes","difficulty","tags"])
    write_csv(os.path.join(CSV_DIR,"ingredients.csv"), ingredients_rows,
              ["ingredient_id","recipe_id","name","quantity","unit","notes"])
    write_csv(os.path.join(CSV_DIR,"steps.csv"), steps_rows,
              ["step_id","recipe_id","step_number","instruction"])
    print("Wrote recipe.csv, ingredients.csv, steps.csv")

def normalize_interactions(interactions_json_path):
    interactions = read_json_file(interactions_json_path)
    rows = []
    for d in interactions:
        rows.append({
            "interaction_id": d.get("_id") or d.get("id") or str(uuid.uuid4()),
            "recipe_id": d.get("recipe_id"),
            "type": d.get("type"),
            "user_id": d.get("user_id"),
            "timestamp": d.get("timestamp"),
            "rating": d.get("rating",""),
            "difficulty_used": d.get("difficulty_used","")
        })
    import csv
    with open(os.path.join(CSV_DIR,"interactions.csv"), "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=["interaction_id","recipe_id","type","user_id","timestamp","rating","difficulty_used"])
        writer.writeheader()
        for r in rows:
            writer.writerow(r)
    print("Wrote interactions.csv")

if __name__ == "__main__":
    normalize_recipes(os.path.join("outputs","raw_json","recipes.json"))
    normalize_interactions(os.path.join("outputs","raw_json","interactions.json"))
