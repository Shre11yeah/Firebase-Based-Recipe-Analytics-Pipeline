📘 Firestore ETL & Analytics Pipeline

A complete end-to-end Data Engineering Pipeline built using the Firebase Firestore Emulator.
This project demonstrates:

🔹 Data modeling

🔹 Firestore seeding (real + synthetic data)

🔹 ETL: Export → Transform → Validate

🔹 Analytics & visual insights

🔹 Clean documentation + reproducible pipeline

🌟 Project Highlights

✔ Works 100% locally (no billing required)

✔ Fully modular Python ETL pipeline

✔ Normalized CSV outputs

✔ Data quality rules + validation report

✔ Analytics with charts and insights

✔ Designed for interviews & real-world demonstration

📂 Project Structure
firestore-etl-project/
│
├── seed_data/               # candidate + synthetic recipes
├── src/                     # ETL + validation + analytics code
├── outputs/                 # JSON, CSV, insights, charts
├── firebase.json            # emulator config
├── .firebaserc              # project config
└── README.md

🧩 Data Model Overview
Entities

Recipes

Users

Interactions

Ingredients

Steps

ERD Diagram
Users (1) ------------ (n) Interactions (n) ------------ (1) Recipes

Recipes (1) ---------- (n) Ingredients
Recipes (1) ---------- (n) Steps

📸 Screenshot: Firestore Emulator (Recipes Collection)

Add your screenshot here:

![C:\Users\ASUS\Desktop\firestore-etl-project\Screenshots\FB-Interactions.jpeg](screenshots/firestore.png)

🚀 How to Run the Pipeline
1️⃣ Start Firestore Emulator
firebase emulators:start --only firestore

2️⃣ Activate Virtual Environment
venv\Scripts\activate

3️⃣ Set Environment Variables
$env:FIRESTORE_EMULATOR_HOST="127.0.0.1:8080"
$env:GOOGLE_CLOUD_PROJECT="demo-firestore"

4️⃣ Seed Firestore
python src\seed_firestore.py


📸 (Add screenshot after seeding)

![Seeding Output](screenshots/seed.png)

5️⃣ Export Firestore → JSON
python src\export_firestore.py

6️⃣ Transform JSON → Normalized CSV
python src\transform_to_csv.py


📸 (Add screenshot of CSV outputs)

![CSV Output](screenshots/csv.png)

7️⃣ Validate Data
python src\validator.py


Generates:

outputs/validation_report.json

8️⃣ Run Analytics
python src\analytics.py


Outputs:

insights.md

Charts (PNG)

📸 (Add chart screenshot)

![Charts](screenshots/charts.png)

📊 Example Insights

Top 10 most frequent ingredients

Most liked recipe

Highest viewed recipe

Difficulty distribution

Prep-time vs likes correlation

Ingredient popularity scoring

User engagement ranking

🧪 Data Validation Rules Applied

Required fields (title, ingredients, steps…)

Positive numeric fields (quantities, minutes)

Valid difficulty values {easy, medium, hard}

Sequential steps

Valid interaction types {view, like, rate}

🏁 Conclusion

This project demonstrates a complete, production-style ETL pipeline using:

Firebase Emulator

Python Data Engineering tools

CSV-based analytics

Validation and quality checks

It is ideal for:

Data Engineering interviews

Portfolio demonstration

Academic submissions

Practical ETL learning