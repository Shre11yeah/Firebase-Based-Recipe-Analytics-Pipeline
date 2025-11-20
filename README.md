📘 Firebase-Based Recipe Analytics Pipeline

A complete end-to-end Data Engineering Pipeline built using the Firebase Firestore Emulator and Python.
This system models recipes and user interactions, seeds Firestore with synthetic data, performs ETL (Export → Transform → Load), validates data quality, and generates analytical insights with visual charts.

🎯 Project Deliverables
✔ 1. Data Modeling

Design entities for Recipes, Ingredients, Steps, Users, and User Interactions

Create an ERD diagram showing all relationships

✔ 2. Firebase Source Data Setup

Add 1 candidate recipe (your own)

Create 15–20 synthetic recipes

Generate user interactions: views, likes, ratings

Seed everything into Firestore Emulator

✔ 3. ETL / ELT Pipeline

Export Firestore collections to JSON

Transform JSON into normalized CSV files:

recipe.csv

ingredients.csv

steps.csv

interactions.csv

Ensure schema consistency during transformation

✔ 4. Data Quality Validation

Check required fields

Detect missing/invalid values

Validate difficulty levels

Check for negative numeric values

Ensure ingredients/steps arrays are not empty

Generate validation_report.json

✔ 5. Analytics

Calculate ingredient frequency

Analyze difficulty distribution

Compute user engagement patterns

Identify most liked & most viewed recipes

Check prep-time vs likes correlation

Generate:

insights.md

PNG charts

✔ 6. Documentation

Complete README with project explanation

Provide folder structure

Add step-by-step running instructions

Include screenshots and output examples

📂 Project Structure
firebase-etl-project/
│
├── seed_data/
│   ├── candidate_recipe.json
│   └── synthetic_recipes.json
│
├── src/
│   ├── seed_firestore.py
│   ├── export_firestore.py
│   ├── transform_to_csv.py
│   ├── validator.py
│   ├── analytics.py
│   └── utils.py
│
├── outputs/
│   ├── raw_json/
│   ├── csv/
│   ├── validation_report.json
│   └── analytics/
│
├── Screenshots/
│   ├── DDistribution.jpeg
│   ├── FB-Interactions.jpeg
│   ├── FB-Recipes.jpeg
│   ├── FB-users.jpeg
│   └── Top-Ingredients.jpeg
│
├── firebase.json
├── .firebaserc
└── README.md

🧩 Data Model (ERD)
Users (1) ----------- (n) Interactions (n) ----------- (1) Recipes

Recipes (1) --------- (n) Ingredients
Recipes (1) --------- (n) Steps

📸 FIRESTORE EMULATOR — SCREENSHOTS
1️⃣ Recipes Collection :
![temp1](https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/Screenshots/FB-Recipes.jpeg)

2️⃣ Users Collection:
![temp1](https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/Screenshots/FB-users.jpeg)

3️⃣ Interactions Collection:
![temp1](https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/Screenshots/FB-Interactions.jpeg)

🚀 How to Run This Project

1️⃣ Start Firestore Emulator
firebase emulators:start --only firestore

2️⃣ Activate Virtual Environment
venv\Scripts\activate

3️⃣ Set Environment Variables
$env:FIRESTORE_EMULATOR_HOST="127.0.0.1:8080"
$env:GOOGLE_CLOUD_PROJECT="demo-firestore"

4️⃣ Seed the Firestore Emulator
python src\seed_firestore.py


This generates:
Recipes
Users
Synthetic interactions

5️⃣ Export Firestore → JSON
python src\export_firestore.py


Output saved in:
outputs/raw_json/

6️⃣ Transform JSON → Normalized CSV
python src\transform_to_csv.py

Example CSV Chart:

7️⃣ Validate Data
python src\validator.py

Creates:
outputs/validation_report.json

8️⃣ Run Analytics
python src\analytics.py

Generates:
Insights (Markdown)
Charts
Example Chart:

📊 Insights Generated

Most frequent ingredients:
![temp1](https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/Screenshots/Top-Ingredients.jpeg)

Highest rated & most-liked recipes
Most viewed recipes

Difficulty breakdown
![temp1](https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/Screenshots/DDistribution.jpeg)

Ingredient popularity
Prep time vs likes correlation
User interaction patterns
Engagement ranking

🧪 Validation Rules
Rule	Description
Required Fields	Title, Ingredients, Steps, Difficulty
Positive Values	Minutes, Quantity
Allowed Difficulty	easy, medium, hard
Non-empty Arrays	Ingredients, Steps
Valid InteractionTypes	view, like, rate

🏁 Conclusion
This project demonstrates a production-ready ETL Data Engineering pipeline using:
1-Firestore (Emulator)
2-Python
3-ETL transformation
4-Data validation
5-Analytical insights

It is ideal for:

🔥 Data Engineering job interviews

🧪 Academic submissions

📊 Portfolio building

🏗 Learning ETL + Firestore