<!-- 📘 Firebase-Based Recipe Analytics Pipeline

A complete end-to-end Data Engineering Pipeline built using the Firebase Firestore Emulator and Python.
This system models recipes and user interactions, seeds Firestore with synthetic data, performs ETL (Export → Transform → Load), validates data quality, and generates analytical insights with visual charts.

🎯 Project Deliverables
✔ 1. Data Modeling
-Design entities for Recipes, Ingredients, Steps, Users, and User Interactions

-Create an ERD diagram showing all relationships

✔ 2. Firebase Source Data Setup
-Add 1 candidate recipe (your own)

-Create 15–20 synthetic recipes

-Generate user interactions: views, likes, ratings

-Seed everything into Firestore Emulator

✔ 3. ETL / ELT Pipeline
-Export Firestore collections to JSON

-Transform JSON into normalized CSV files:

-recipe.csv

-ingredients.csv

-steps.csv

-interactions.csv

-Ensure schema consistency during transformation

✔ 4. Data Quality Validation
-Check required fields

-Detect missing/invalid values

-Validate difficulty levels

-Check for negative numeric values

-Ensure ingredients/steps arrays are not empty

-Generate validation_report.json

✔ 5. Analytics
-Calculate ingredient frequency

-Analyze difficulty distribution

-Compute user engagement patterns

-Identify most liked & most viewed recipes

-Check prep-time vs likes correlation

-Generate: => insights.md
-PNG charts

✔ 6. Documentation
-Complete README with project explanation

-Provide folder structure

-Add step-by-step running instructions

-Include screenshots and output examples

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
$env:FIRESTORE_EMULATOR_HOST="000.0.0.0:HOSTNO"
$env:GOOGLE_CLOUD_PROJECT="demo-firestore"

4️⃣ Seed the Firestore Emulator
python src\seed_firestore.py


This generates:
-Recipes
-Users
-Synthetic interactions

5️⃣ Export Firestore → JSON
python src\export_firestore.py

Output saved in:
outputs/raw_json/

6️⃣ Transform JSON → Normalized CSV
python src\transform_to_csv.py

Example CSV Chart:
![temp1](https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/Screenshots/CSV.jpeg)

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

🏗 Learning ETL + Firestore -->


📘 <span style="font-size:32px;">Firebase-Based Recipe Analytics Pipeline</span>
<p> A complete end-to-end <b>Data Engineering Pipeline</b> built using the Firebase Firestore Emulator and Python. This system models recipes & user interactions, seeds Firestore with synthetic data, performs ETL, validates data, and generates analytical insights with visual charts. </p>
<span style="font-size:26px;">🎯 Project Deliverables</span>
✔ <b>1. Data Modeling</b>
<ul> <li>Design entities for <b>Recipes, Ingredients, Steps, Users, Interactions</b></li> <li>Create an <b>ERD diagram</b> showing relationships</li> </ul>
✔ <b>2. Firebase Source Data Setup</b>
<ul> <li>Add <b>1 candidate recipe</b></li> <li>Create <b>15–20 synthetic recipes</b></li> <li>Generate interactions: <b>views, likes, ratings</b></li> <li>Seed everything into the <b>Firestore Emulator</b></li> </ul>
✔ <b>3. ETL / ELT Pipeline</b>
<ul> <li>Export Firestore → <b>JSON</b></li> <li>Transform JSON → <b>Normalized CSV</b></li> </ul>

<b>Generated CSVs:</b>

recipe.csv

ingredients.csv

steps.csv

interactions.csv

✔ <b>4. Data Quality Validation</b>
<ul> <li>Check required fields</li> <li>Detect missing or invalid values</li> <li>Difficulty-level validation</li> <li>Negative numeric values check</li> <li>Ingredients/steps non-empty</li> <li>Generates <code>validation_report.json</code></li> </ul>
✔ <b>5. Analytics</b>
<ul> <li>Ingredient frequency</li> <li>Difficulty distribution</li> <li>User engagement patterns</li> <li>Most liked & most viewed recipes</li> <li>Prep time vs likes correlation</li> <li>Generates <code>insights.md</code> + charts (PNG)</li> </ul>
✔ <b>6. Documentation</b>
<ul> <li>README</li> <li>Folder structure</li> <li>How-to-run instructions</li> <li>Screenshots and examples</li> </ul>
<span style="font-size:26px;">📂 Project Structure</span>
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

🧩 <span style="font-size:26px;">Data Model (ERD)</span>
Users (1) ----------- (n) Interactions (n) ----------- (1) Recipes

Recipes (1) --------- (n) Ingredients
Recipes (1) --------- (n) Steps

📸 <span style="font-size:26px;">Firestore Emulator — Screenshots</span>

<b>1️⃣ Recipes Collection</b>
<img src="https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/Screenshots/FB-Recipes.jpeg" width="600"/>

<br/>

<b>2️⃣ Users Collection</b>
<img src="https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/Screenshots/FB-users.jpeg" width="600"/>

<br/>

<b>3️⃣ Interactions Collection</b>
<img src="https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/Screenshots/FB-Interactions.jpeg" width="600"/>

🚀 <span style="font-size:26px;">How to Run This Project</span>
<b>1️⃣ Start Firestore Emulator</b>
firebase emulators:start --only firestore

<b>2️⃣ Activate Virtual Environment</b>
venv\Scripts\activate

<b>3️⃣ Set Environment Variables</b>
$env:FIRESTORE_EMULATOR_HOST="000.0.0.0:HOSTNO"
$env:GOOGLE_CLOUD_PROJECT="demo-firestore"

<b>4️⃣ Seed Firestore</b>
python src/seed_firestore.py


This generates:

Recipes

Users

Synthetic interactions

<b>5️⃣ Export Firestore → JSON</b>
python src/export_firestore.py


Output in:

outputs/raw_json/

<b>6️⃣ Transform JSON → CSV</b>
python src/transform_to_csv.py


<b>Example Output:</b>
<img src="https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/Screenshots/CSV.jpeg" width="600"/>

<b>7️⃣ Validate Data</b>
python src/validator.py


Creates:

outputs/validation_report.json

<b>8️⃣ Run Analytics</b>
python src/analytics.py


Generates Markdown insights + charts.

📊 <span style="font-size:26px;">Insights Generated</span>

<b>Most Frequent Ingredients</b>
<img src="https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/Screenshots/Top-Ingredients.jpeg" width="600"/>

<b>Difficulty Distribution</b>
<img src="https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/Screenshots/DDistribution.jpeg" width="600"/>

Includes:

Highest rated recipes

Most viewed recipes

Ingredient popularity

Prep time vs likes

Engagement patterns

🧪 <span style="font-size:26px;">Validation Rules</span>
<table> <tr><th>Rule</th><th>Description</th></tr> <tr><td>Required Fields</td><td>Title, Ingredients, Steps, Difficulty</td></tr> <tr><td>Positive Values</td><td>Time, Quantity</td></tr> <tr><td>Allowed Difficulty</td><td>easy, medium, hard</td></tr> <tr><td>Non-empty Arrays</td><td>Ingredients, Steps</td></tr> <tr><td>Interaction Types</td><td>view, like, rate</td></tr> </table>
🏁 <span style="font-size:26px;">Conclusion</span>

This project demonstrates a production-grade Data Engineering ETL Pipeline using:

Firestore (Emulator)

Python

ETL transformations

Data validation

Analytics & insights

Perfect for:
🔥 Data Engineering interviews
📊 Portfolio projects
🧪 Academic submissions
🏗 Learning ETL + Firebase