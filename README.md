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

<div align="center">

📘 <span style="font-size:38px; font-weight:700;">Firebase-Based Recipe Analytics Pipeline</span>

<p style="font-size:17px; max-width:800px;">
A complete end-to-end <b>Data Engineering Pipeline</b> built using the <b>Firebase Firestore Emulator</b> and <b>Python</b>.  
This system seeds Firestore with synthetic recipe data, performs ETL, validates data quality, and generates analytical insights with visual charts.
</p>

</div>

---

## <span style="font-size:28px; font-weight:600;">🎯 Project Deliverables</span>

### ✔ <span style="font-size:22px;">1. Data Modeling</span>
- Designed entities for Recipes, Ingredients, Steps, Users, Interactions  
- Created a clear ERD (Entity Relationship Diagram)

### ✔ <span style="font-size:22px;">2. Firebase Source Data Setup</span>
- 1 personal candidate recipe  
- 15–20 synthetic recipes  
- User interactions (views, likes, ratings)  
- Data seeded into Firestore Emulator

### ✔ <span style="font-size:22px;">3. ETL / ELT Pipeline</span>
- Export Firestore ➝ JSON  
- Transform JSON ➝ Normalized CSVs  

**Output files:**  
- recipe.csv  
- ingredients.csv  
- steps.csv  
- interactions.csv

### ✔ <span style="font-size:22px;">4. Data Quality Validation</span>
- Required field checks  
- Missing/invalid values detection  
- Difficulty validation  
- No negative values  
- Ingredients/Steps must be non-empty  
- Output → validation_report.json

### ✔ <span style="font-size:22px;">5. Analytics</span>
- Ingredient frequency  
- Difficulty distribution  
- Most liked / viewed recipes  
- Engagement patterns  
- Prep-time vs likes  
- Generates insights + PNG charts

### ✔ <span style="font-size:22px;">6. Documentation</span>
- README (this file)  
- Folder structure  
- How to run  
- Screenshots & outputs  

---

## 📂 <span style="font-size:28px; font-weight:600;">Project Structure</span>

firebase-etl-project/
│
├── seed_data/
│ ├── candidate_recipe.json
│ └── synthetic_recipes.json
│
├── src/
│ ├── seed_firestore.py
│ ├── export_firestore.py
│ ├── transform_to_csv.py
│ ├── validator.py
│ ├── analytics.py
│ └── utils.py
│
├── outputs/
│ ├── raw_json/
│ ├── csv/
│ ├── validation_report.json
│ └── analytics/
│
├── Screenshots/
│ ├── DDistribution.jpeg
│ ├── FB-Interactions.jpeg
│ ├── FB-Recipes.jpeg
│ ├── FB-users.jpeg
│ └── Top-Ingredients.jpeg
│
├── firebase.json
├── .firebaserc
└── README.md

---

## 🧩 <span style="font-size:28px; font-weight:600;">Data Model (ERD)</span>

Users (1) ----------- (n) Interactions (n) ----------- (1) Recipes

Recipes (1) --------- (n) Ingredients
Recipes (1) --------- (n) Steps

---

## 📸 <span style="font-size:28px; font-weight:600;">Firestore Emulator Screenshots</span>

### **1️⃣ Recipes Collection**
<img src="https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/Screenshots/FB-Recipes.jpeg" width="650"/>

### **2️⃣ Users Collection**
<img src="https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/Screenshots/FB-users.jpeg" width="650"/>

### **3️⃣ Interactions Collection**
<img src="https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/Screenshots/FB-Interactions.jpeg" width="650"/>

---

## 🚀 How to Run This Project

### **1️⃣ Start Firestore Emulator**
```bash
firebase emulators:start --only firestore
2️⃣ Activate Virtual Environment
bash
Copy code
venv\Scripts\activate
3️⃣ Set Environment Variables (PowerShell)
bash
Copy code
$env:FIRESTORE_EMULATOR_HOST="000.0.0.0:HOSTNO"
$env:GOOGLE_CLOUD_PROJECT="demo-firestore"
4️⃣ Seed Firestore
bash
Copy code
python src/seed_firestore.py
Generates:

Recipes

Users

Synthetic interactions

5️⃣ Export Firestore → JSON
bash
Copy code
python src/export_firestore.py
Output saved in:
outputs/raw_json/

6️⃣ Transform JSON → Normalized CSV
bash
Copy code
python src/transform_to_csv.py
<img src="https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/Screenshots/CSV.jpeg" width="650"/>
7️⃣ Validate Data
bash
Copy code
python src/validator.py
Creates:
outputs/validation_report.json

8️⃣ Run Analytics
bash
Copy code
python src/analytics.py
Outputs:

insights.md

PNG charts

📊 <span style="font-size:28px; font-weight:600;">Analytics Output</span>
Most Frequent Ingredients
<img src="https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/Screenshots/Top-Ingredients.jpeg" width="650"/>
Difficulty Distribution
<img src="https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/Screenshots/DDistribution.jpeg" width="650"/>
🧪 <span style="font-size:28px; font-weight:600;">Validation Rules</span>
<table> <tr><th>Rule</th><th>Description</th></tr> <tr><td>Required Fields</td><td>Title, Ingredients, Steps, Difficulty</td></tr> <tr><td>Positive Values</td><td>Time, Quantity must be ≥ 0</td></tr> <tr><td>Difficulty Levels</td><td>easy, medium, hard</td></tr> <tr><td>Non-empty Arrays</td><td>Ingredients, Steps</td></tr> <tr><td>Interaction Types</td><td>view, like, rate</td></tr> </table>
🏁 <span style="font-size:28px; font-weight:600;">Conclusion</span>
This project demonstrates a production-ready Data Engineering ETL Pipeline using:

🔥 Firebase Firestore (Emulator)
🐍 Python
🛠 ETL Transformation
🧪 Data Validation
📊 Analytics & Reporting