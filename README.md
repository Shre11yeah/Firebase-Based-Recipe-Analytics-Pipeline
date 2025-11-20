# Firestore ETL Project (Local emulator)

## Goal
Assess candidate's ability to design and implement a data pipeline using Firestore as source. This repo seeds Firestore (local emulator), exports, transforms, validates, and analyzes recipe data.

## Structure
(see folder layout in repository)

## Prereqs
- Node.js
- firebase-tools (`npm i -g firebase-tools`)
- Python3, pip
- Create and activate a Python venv, then `pip install -r requirements.txt`

## Running (local, no billing)
1. Start Firestore emulator:
   `firebase emulators:start --only firestore`

2. In a new terminal:

export FIRESTORE_EMULATOR_HOST="127.0.0.1:8080"
export GOOGLE_CLOUD_PROJECT="local-project"
source venv/bin/activate



3. Edit `seed_data/candidate_recipe.json` — replace with your own recipe.

4. Seed the emulator:
`python3 src/seed_firestore.py`

5. Export:
`python3 src/export_firestore.py`

6. Transform:
`python3 src/transform_to_csv.py`

7. Validate:
`python3 src/validator.py`

8. Analytics:
`python3 src/analytics.py`

## ETL overview
- `seed_firestore.py`: creates recipes, users, interactions
- `export_firestore.py`: reads collections and writes JSON
- `transform_to_csv.py`: normalizes JSON into `recipe.csv`, `ingredients.csv`, `steps.csv`, `interactions.csv`
- `validator.py`: applies quality rules and writes `outputs/validation_report.json`
- `analytics.py`: computes insights & charts

## Validation rules implemented
- Required fields present (recipe_id, title, ingredient name, step instruction)
- Numeric fields non-negative (prep, cook, total minutes)
- Non-empty arrays for ingredients/steps are enforced through presence checks
- `difficulty` must be one of `easy|medium|hard`

## Analytics summary
Find `outputs/analytics/insights.md` for the generated insights:
- Most common ingredients
- Average prep time
- Difficulty distribution
- Correlation between prep time and likes
- Most viewed recipes
- Ingredients associated with high engagement
- Top liked recipes
- Average rating per recipe (if available)
- Views per minute
- Users with most attempts

## Known constraints / limitations
- All operations run against the **Firestore emulator** (local). If you want to use real Firestore, configure `GOOGLE_APPLICATION_CREDENTIALS` and remove emulator env var.
- Exporting to Cloud Firestore managed backups (gcloud `firestore export`) requires cloud access and billing; we used local emulator and SDK reads instead.
- Synthetic data generator is simple and not domain exhaustive — adapt as needed.
