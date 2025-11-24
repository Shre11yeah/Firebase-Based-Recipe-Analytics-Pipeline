# validator.py
"""
Validates CSVs according to rules:
 - Required fields present (recipe_id, title, ingredients non-empty, steps non-empty)
 - Numeric fields non-negative (prep_minutes, cook_minutes, total_minutes, servings)
 - difficulty is one of allowed set
Generates outputs/validation_report.json
"""
import csv, json, os
from collections import defaultdict

CSV_DIR = os.path.join("outputs","csv")
REPORT_PATH = os.path.join("outputs","validation_report.json")
ALLOWED_DIFFICULTIES = {"easy","medium","hard"}

def validate_recipes():
    problems = []
    valid_count = 0
    path = os.path.join(CSV_DIR,"recipe.csv")
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rid = row.get("recipe_id")
            row_problems = []
            if not rid:
                row_problems.append("missing recipe_id")
            if not row.get("title"):
                row_problems.append("missing title")
            # numeric checks
            try:
                if row.get("prep_minutes"):
                    if float(row["prep_minutes"]) < 0: row_problems.append("prep_minutes negative")
            except:
                row_problems.append("prep_minutes not numeric")
            try:
                if row.get("cook_minutes"):
                    if float(row["cook_minutes"]) < 0: row_problems.append("cook_minutes negative")
            except:
                row_problems.append("cook_minutes not numeric")
            try:
                if row.get("total_minutes"):
                    if float(row["total_minutes"]) < 0: row_problems.append("total_minutes negative")
            except:
                row_problems.append("total_minutes not numeric")
            diff = (row.get("difficulty") or "").lower()
            if diff and diff not in ALLOWED_DIFFICULTIES:
                row_problems.append(f"invalid difficulty: {diff}")
            if row_problems:
                problems.append({"recipe_id": rid, "problems": row_problems})
            else:
                valid_count += 1
    return valid_count, problems

def validate_ingredients():
    problems = []
    valid = 0
    path = os.path.join(CSV_DIR,"ingredients.csv")
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row_problems = []
            if not row.get("recipe_id"): row_problems.append("missing recipe_id")
            if not row.get("name"): row_problems.append("missing ingredient name")
            if row_problems:
                problems.append({"ingredient_id": row.get("ingredient_id"), "problems": row_problems})
            else:
                valid += 1
    return valid, problems

def validate_steps():
    problems = []
    valid = 0
    path = os.path.join(CSV_DIR,"steps.csv")
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rp = []
            if not row.get("recipe_id"): rp.append("missing recipe_id")
            if not row.get("instruction"): rp.append("missing instruction")
            if rp:
                problems.append({"step_id": row.get("step_id"), "problems": rp})
            else:
                valid += 1
    return valid, problems

def validate_interactions():
    problems=[]
    valid=0
    path=os.path.join(CSV_DIR,"interactions.csv")
    with open(path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            rp=[]
            if not row.get("recipe_id"): rp.append("missing recipe_id")
            if not row.get("type"): rp.append("missing type")
            if rp:
                problems.append({"interaction_id": row.get("interaction_id"), "problems": rp})
            else:
                valid += 1
    return valid, problems

if __name__ == "__main__":
    report = {}
    v_r, p_r = validate_recipes()
    v_i, p_i = validate_ingredients()
    v_s, p_s = validate_steps()
    v_in, p_in = validate_interactions()
    report["recipes_valid_count"] = v_r
    report["recipes_invalid"] = p_r
    report["ingredients_valid_count"] = v_i
    report["ingredients_invalid"] = p_i
    report["steps_valid_count"] = v_s
    report["steps_invalid"] = p_s
    report["interactions_valid_count"] = v_in
    report["interactions_invalid"] = p_in
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2)
    print("Validation complete. Report:", REPORT_PATH)
