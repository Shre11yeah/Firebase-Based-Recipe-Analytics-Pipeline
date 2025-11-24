<!-- # 🔥 Firebase-Based Recipe Analytics Pipeline

A complete end-to-end **Data Engineering Pipeline** built using **Firebase Firestore Emulator** and **Python**. This system seeds Firestore with synthetic recipe data, performs ETL transformations, validates data quality, and generates analytical insights with visual charts.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Firebase](https://img.shields.io/badge/Firebase-Emulator-orange.svg)](https://firebase.google.com/docs/emulator-suite)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Project Structure](#-project-structure)
- [Data Model](#-data-model)
- [Installation](#-installation)
- [Usage](#-usage)
- [Analytics Output](#-analytics-output)
- [Validation Rules](#-validation-rules)
- [Screenshots](#-screenshots)
- [Technologies Used](#-technologies-used)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Project Overview

This project demonstrates a **production-ready data engineering workflow** that includes:

- **Data Modeling**: Designed normalized entities for recipes, ingredients, steps, users, and interactions
- **Data Generation**: Synthetic recipe data with realistic user interactions
- **ETL Pipeline**: Extract from Firestore → Transform to normalized CSV → Load for analytics
- **Data Quality**: Comprehensive validation checks ensuring data integrity
- **Analytics**: Automated insights generation with visualization charts

---

## ✨ Features

### 1. **Data Modeling**
- Entity-Relationship Design (ERD)
- Normalized data structure
- Collections: Recipes, Users, Interactions, Ingredients, Steps

### 2. **Firebase Source Data Setup**
- 1 personal candidate recipe
- 15-20 synthetic recipes
- Realistic user interaction patterns (views, likes, ratings)
- Data seeded into Firestore Emulator

### 3. **ETL/ELT Pipeline**
- **Extract**: Export Firestore collections to JSON
- **Transform**: Normalize JSON into relational CSV format
- **Load**: Prepare data for analytics and reporting

**Output CSV Files:**
```
├── recipe.csv
├── ingredients.csv
├── steps.csv
└── interactions.csv
```

### 4. **Data Quality Validation**
- Required field presence checks
- Missing/invalid value detection
- Difficulty level validation (`easy`, `medium`, `hard`)
- Non-negative value constraints
- Array emptiness checks (ingredients, steps)
- Interaction type validation
- Output: `validation_report.json`

### 5. **Analytics & Insights**
- Top ingredient frequency analysis
- Recipe difficulty distribution
- Most liked/viewed recipes ranking
- User engagement patterns
- Preparation time vs. popularity correlation
- Automated chart generation (PNG format)
- Markdown insights report

### 6. **Comprehensive Documentation**
- Detailed README with instructions
- Clear folder organization
- Step-by-step execution guide
- Visual screenshots of outputs

---

## 🏗 Architecture

```
┌─────────────────┐
│ Seed Data       │
│ (JSON Files)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Firestore       │
│ Emulator        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Export to JSON  │
│ (Raw Data)      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Transform to    │
│ CSV (Normalized)│
└────────┬────────┘
         │
         ├─────────────┐
         ▼             ▼
┌─────────────┐  ┌──────────────┐
│ Validator   │  │ Analytics    │
│             │  │              │
└─────────────┘  └──────────────┘
```

---

## 📂 Project Structure

```
firebase-etl-project/
│
├── seed_data/
│   ├── candidate_recipe.json       # Your personal recipe
│   └── synthetic_recipes.json      # Generated test data
│
├── src/
│   ├── seed_firestore.py          # Seeds Firestore with initial data
│   ├── export_firestore.py        # Exports collections to JSON
│   ├── transform_to_csv.py        # Transforms JSON to normalized CSV
│   ├── validator.py               # Data quality validation
│   ├── analytics.py               # Generates insights and charts
│   └── utils.py                   # Helper functions
│
├── outputs/
│   ├── raw_json/                  # Exported Firestore data
│   ├── csv/                       # Normalized CSV files
│   ├── validation_report.json     # Data quality report
│   └── analytics/                 # Charts and insights
│
├── Screenshots/                    # Project screenshots
│   ├── DDistribution.jpeg
│   ├── FB-Interactions.jpeg
│   ├── FB-Recipes.jpeg
│   ├── FB-users.jpeg
│   └── Top-Ingredients.jpeg
│
├── firebase.json                   # Firebase configuration
├── .firebaserc                     # Firebase project settings
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

---

## 🧩 Data Model

### Entity Relationship Diagram (ERD)

```
Users (1) ────────── (n) Interactions (n) ────────── (1) Recipes
                                              │
                                              ├── (n) Ingredients
                                              └── (n) Steps
```

### Collections Schema

**Recipes**
- `recipe_id` (string, primary key)
- `title` (string)
- `difficulty` (string: easy/medium/hard)
- `prep_time` (integer, minutes)
- `cook_time` (integer, minutes)
- `servings` (integer)
- `created_at` (timestamp)

**Ingredients**
- `ingredient_id` (string, primary key)
- `recipe_id` (string, foreign key)
- `name` (string)
- `quantity` (float)
- `unit` (string)

**Steps**
- `step_id` (string, primary key)
- `recipe_id` (string, foreign key)
- `step_number` (integer)
- `instruction` (string)

**Users**
- `user_id` (string, primary key)
- `username` (string)
- `email` (string)
- `joined_date` (timestamp)

**Interactions**
- `interaction_id` (string, primary key)
- `user_id` (string, foreign key)
- `recipe_id` (string, foreign key)
- `interaction_type` (string: view/like/rate)
- `rating` (integer, 1-5, optional)
- `timestamp` (timestamp)

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- Node.js and npm
- Firebase CLI

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/firebase-recipe-analytics.git
cd firebase-recipe-analytics
```

### Step 2: Install Firebase CLI

```bash
npm install -g firebase-tools
```

### Step 3: Set Up Python Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 4: Initialize Firebase Project

```bash
firebase init firestore
```

---

## 💻 Usage

### Step 1: Start Firestore Emulator

```bash
firebase emulators:start --only firestore
```

The emulator will start on `localhost:8080` (default).

### Step 2: Set Environment Variables

**Windows (PowerShell):**
```powershell
$env:FIRESTORE_EMULATOR_HOST="127.0.0.1:8080"
$env:GOOGLE_CLOUD_PROJECT="demo-firestore"
```

**macOS/Linux (Bash):**
```bash
export FIRESTORE_EMULATOR_HOST="127.0.0.1:8080"
export GOOGLE_CLOUD_PROJECT="demo-firestore"
```

### Step 3: Seed Firestore with Data

```bash
python src/seed_firestore.py
```

This generates:
- Recipe documents
- User profiles
- Synthetic user interactions

### Step 4: Export Firestore to JSON

```bash
python src/export_firestore.py
```

Output saved in: `outputs/raw_json/`

### Step 5: Transform JSON to Normalized CSV

```bash
python src/transform_to_csv.py
```

Creates normalized CSV files in: `outputs/csv/`

### Step 6: Validate Data Quality

```bash
python src/validator.py
```

Generates: `outputs/validation_report.json`

### Step 7: Run Analytics

```bash
python src/analytics.py
```

Outputs:
- `outputs/analytics/insights.md` - Detailed insights report
- `outputs/analytics/*.png` - Visualization charts

---

## 📊 Analytics Output

### Generated Insights

1. **Top 10 Most Frequent Ingredients**
   - Bar chart showing ingredient usage across all recipes
   
2. **Recipe Difficulty Distribution**
   - Pie chart of easy/medium/hard recipe breakdown
   
3. **Most Liked Recipes**
   - Ranking of recipes by user engagement
   
4. **Most Viewed Recipes**
   - Top recipes by view count
   
5. **Engagement Patterns**
   - Time-series analysis of user interactions
   
6. **Prep Time vs Popularity**
   - Scatter plot correlating preparation time with likes

### Sample Output

![Top Ingredients](Screenshots/Top-Ingredients.jpeg)
![Difficulty Distribution](Screenshots/DDistribution.jpeg)

---

## 🧪 Validation Rules

| Rule | Description |
|------|-------------|
| **Required Fields** | Title, Ingredients, Steps, Difficulty must be present |
| **Positive Values** | Time values and quantities must be ≥ 0 |
| **Difficulty Levels** | Must be one of: `easy`, `medium`, `hard` |
| **Non-empty Arrays** | Ingredients and Steps must contain at least one item |
| **Interaction Types** | Must be one of: `view`, `like`, `rate` |
| **Rating Range** | If present, rating must be between 1-5 |
| **Foreign Keys** | All referenced IDs must exist in parent collections |

---

## 📸 Screenshots

### Firestore Emulator - Recipes Collection
![Recipes Collection](Screenshots/FB-Recipes.jpeg)

### Firestore Emulator - Users Collection
![Users Collection](Screenshots/FB-users.jpeg)

### Firestore Emulator - Interactions Collection
![Interactions Collection](Screenshots/FB-Interactions.jpeg)

---

## 🛠 Technologies Used

- **Firebase Firestore Emulator** - NoSQL document database
- **Python 3.8+** - Primary programming language
- **Pandas** - Data manipulation and analysis
- **Matplotlib/Seaborn** - Data visualization
- **Firebase Admin SDK** - Firestore interaction
- **JSON** - Data interchange format
- **CSV** - Structured data export

### Python Libraries

```
firebase-admin
pandas
matplotlib
seaborn
python-dotenv
```

---
 -->


# 🔥 Firebase-Based Recipe Analytics Pipeline

A complete end-to-end **Data Engineering Pipeline** built using **Firebase Firestore Emulator** and **Python**. This system seeds Firestore with synthetic recipe data, performs ETL transformations, validates data quality, and generates analytical insights with visual charts.

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Firebase](https://img.shields.io/badge/Firebase-Emulator-orange.svg)](https://firebase.google.com/docs/emulator-suite)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 📋 Table of Contents

- [Project Overview](#-project-overview)
- [Features](#-features)
- [Architecture](#-architecture)
- [Project Structure](#-project-structure)
- [Data Model](#-data-model)
- [Installation](#-installation)
- [Usage](#-usage)
- [Analytics Output](#-analytics-output)
- [Validation Rules](#-validation-rules)
- [Screenshots](#-screenshots)
- [Technologies Used](#-technologies-used)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🎯 Project Overview

This project demonstrates a **production-ready data engineering workflow** that includes:

- **Data Modeling**: Designed normalized entities for recipes, ingredients, steps, users, and interactions
- **Data Generation**: Synthetic recipe data with realistic user interactions
- **ETL Pipeline**: Extract from Firestore → Transform to normalized CSV → Load for analytics
- **Data Quality**: Comprehensive validation checks ensuring data integrity
- **Analytics**: Automated insights generation with visualization charts

---

## ✨ Features

### 1. **Data Modeling**
- Entity-Relationship Design (ERD)
- Normalized data structure
- Collections: Recipes, Users, Interactions, Ingredients, Steps

### 2. **Firebase Source Data Setup**
- 1 personal candidate recipe
- 15-20 synthetic recipes
- Realistic user interaction patterns (views, likes, ratings)
- Data seeded into Firestore Emulator

### 3. **ETL/ELT Pipeline**
- **Extract**: Export Firestore collections to JSON
- **Transform**: Normalize JSON into relational CSV format
- **Load**: Prepare data for analytics and reporting

**Output CSV Files:**
```
├── recipe.csv
├── ingredients.csv
├── steps.csv
└── interactions.csv
```

### 4. **Data Quality Validation**
- Required field presence checks
- Missing/invalid value detection
- Difficulty level validation (`easy`, `medium`, `hard`)
- Non-negative value constraints
- Array emptiness checks (ingredients, steps)
- Interaction type validation
- Output: `validation_report.json`

### 5. **Analytics & Insights**
- Top ingredient frequency analysis
- Recipe difficulty distribution
- Most liked/viewed recipes ranking
- User engagement patterns
- Preparation time vs. popularity correlation
- Recipe similarity analysis
- Hourly interaction trends
- Tag distribution analysis
- Active user tracking
- Engagement scoring
- Ingredient co-occurrence heatmap
- Interactive word clouds
- Automated chart generation (PNG format)
- Markdown insights report

### 6. **Comprehensive Documentation**
- Detailed README with instructions
- Clear folder organization
- Step-by-step execution guide
- Visual screenshots of outputs

---

## 🏗 Architecture

```
┌─────────────────┐
│ Seed Data       │
│ (JSON Files)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Firestore       │
│ Emulator        │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Export to JSON  │
│ (Raw Data)      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Transform to    │
│ CSV (Normalized)│
└────────┬────────┘
         │
         ├─────────────┐
         ▼             ▼
┌─────────────┐  ┌──────────────┐
│ Validator   │  │ Analytics    │
│             │  │              │
└─────────────┘  └──────────────┘
```

---

## 📂 Project Structure

```
firebase-etl-project/
│
├── seed_data/
│   ├── candidate_recipe.json       # Your personal recipe
│   └── synthetic_recipes.json      # Generated test data
│
├── src/
│   ├── seed_firestore.py          # Seeds Firestore with initial data
│   ├── export_firestore.py        # Exports collections to JSON
│   ├── transform_to_csv.py        # Transforms JSON to normalized CSV
│   ├── validator.py               # Data quality validation
│   ├── analytics.py               # Generates insights and charts
│   └── utils.py                   # Helper functions
│
├── outputs/
│   ├── raw_json/                  # Exported Firestore data
│   ├── csv/                       # Normalized CSV files
│   ├── validation_report.json     # Data quality report
│   └── analytics/                 # Charts and insights
│       └── charts/                # Visualization images
│
├── Screenshots/                    # Project screenshots
│   ├── DDistribution.jpeg
│   ├── FB-Interactions.jpeg
│   ├── FB-Recipes.jpeg
│   ├── FB-users.jpeg
│   └── Top-Ingredients.jpeg
│
├── firebase.json                   # Firebase configuration
├── .firebaserc                     # Firebase project settings
├── requirements.txt                # Python dependencies
└── README.md                       # This file
```

---

## 🧩 Data Model

### Entity Relationship Diagram (ERD)

```
Users (1) ────────── (n) Interactions (n) ────────── (1) Recipes
                                              │
                                              ├── (n) Ingredients
                                              └── (n) Steps
```

### Collections Schema

**Recipes**
- `recipe_id` (string, primary key)
- `title` (string)
- `difficulty` (string: easy/medium/hard)
- `prep_time` (integer, minutes)
- `cook_time` (integer, minutes)
- `servings` (integer)
- `created_at` (timestamp)

**Ingredients**
- `ingredient_id` (string, primary key)
- `recipe_id` (string, foreign key)
- `name` (string)
- `quantity` (float)
- `unit` (string)

**Steps**
- `step_id` (string, primary key)
- `recipe_id` (string, foreign key)
- `step_number` (integer)
- `instruction` (string)

**Users**
- `user_id` (string, primary key)
- `username` (string)
- `email` (string)
- `joined_date` (timestamp)

**Interactions**
- `interaction_id` (string, primary key)
- `user_id` (string, foreign key)
- `recipe_id` (string, foreign key)
- `interaction_type` (string: view/like/rate)
- `rating` (integer, 1-5, optional)
- `timestamp` (timestamp)

---

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- Node.js and npm
- Firebase CLI

### Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/firebase-recipe-analytics.git
cd firebase-recipe-analytics
```

### Step 2: Install Firebase CLI

```bash
npm install -g firebase-tools
```

### Step 3: Set Up Python Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 4: Initialize Firebase Project

```bash
firebase init firestore
```

---

## 💻 Usage

### Step 1: Start Firestore Emulator

```bash
firebase emulators:start --only firestore
```

The emulator will start on `localhost:8080` (default).

### Step 2: Set Environment Variables

**Windows (PowerShell):**
```powershell
$env:FIRESTORE_EMULATOR_HOST="127.0.0.1:8080"
$env:GOOGLE_CLOUD_PROJECT="demo-firestore"
```

**macOS/Linux (Bash):**
```bash
export FIRESTORE_EMULATOR_HOST="127.0.0.1:8080"
export GOOGLE_CLOUD_PROJECT="demo-firestore"
```

### Step 3: Seed Firestore with Data

```bash
python src/seed_firestore.py
```

This generates:
- Recipe documents
- User profiles
- Synthetic user interactions

### Step 4: Export Firestore to JSON

```bash
python src/export_firestore.py
```

Output saved in: `outputs/raw_json/`

### Step 5: Transform JSON to Normalized CSV

```bash
python src/transform_to_csv.py
```

Creates normalized CSV files in: `outputs/csv/`

### Step 6: Validate Data Quality

```bash
python src/validator.py
```

Generates: `outputs/validation_report.json`

### Step 7: Run Analytics

```bash
python src/analytics.py
```

Outputs:
- `outputs/analytics/insights.md` - Detailed insights report
- `outputs/analytics/charts/*.png` - Visualization charts

---

## 📊 Analytics Output

### Generated Insights & Visualizations

The analytics pipeline generates comprehensive visual insights to understand recipe patterns, user behavior, and engagement metrics. Below are all the generated charts:

#### 1. **Ingredient Analysis**

<img src="https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/src/outputs/analytics/charts/top_ingredients.png" alt="Top Ingredients" width="500"/>

**Top 10 Most Frequent Ingredients** - Bar chart showing the most commonly used ingredients across all recipes.

<img src="https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/src/outputs/analytics/charts/ingredient_wordcloud.png" alt="Ingredient Word Cloud" width="500"/>

**Ingredient Word Cloud** - Visual representation of ingredient popularity with size indicating frequency.

<img src="https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/src/outputs/analytics/charts/ingredient_heatmap.png" alt="Ingredient Co-occurrence Heatmap" width="500"/>

**Ingredient Co-occurrence Heatmap** - Shows which ingredients are commonly used together in recipes.

#### 2. **Recipe Difficulty & Performance**

<img src="https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/src/outputs/analytics/charts/difficulty_dist.png" alt="Difficulty Distribution" width="500"/>

**Recipe Difficulty Distribution** - Pie chart showing the breakdown of recipes by difficulty level (easy/medium/hard).

<img src="https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/src/outputs/analytics/charts/difficulty_vs_rating.png" alt="Difficulty vs Rating" width="500"/>

**Difficulty vs Average Rating** - Analysis of how recipe difficulty correlates with user ratings.

#### 3. **User Engagement Metrics**

<img src="https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/src/outputs/analytics/charts/likes_vs_views.png" alt="Likes vs Views" width="500"/>

**Likes vs Views Scatter Plot** - Correlation between recipe views and likes to identify engagement patterns.

<img src="https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/src/outputs/analytics/charts/attempts_vs_likes.png" alt="Attempts vs Likes" width="500"/>

**Recipe Attempts vs Likes** - Relationship between how often recipes are attempted and their like count.

<img src="https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/src/outputs/analytics/charts/engagement_score.png" alt="Engagement Score" width="500"/>

**Recipe Engagement Score** - Composite metric ranking recipes by overall user engagement.

#### 4. **Time & Popularity Analysis**

<img src="https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/src/outputs/analytics/charts/prep_time_vs_likes.png" alt="Prep Time vs Likes" width="500"/>

**Preparation Time vs Popularity** - Scatter plot showing how prep time affects recipe likes.

<img src="https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/src/outputs/analytics/charts/hourly_trend.png" alt="Hourly Interaction Trends" width="500"/>

**Hourly Interaction Trends** - Line chart showing peak usage hours for recipe interactions.

#### 5. **User Behavior & Activity**

<img src="https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/src/outputs/analytics/charts/active_users.png" alt="Active Users" width="500"/>

**Active Users Over Time** - Tracking user activity patterns and engagement trends.

#### 6. **Content Classification**

<img src="https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/src/outputs/analytics/charts/tags_distribution.png" alt="Tags Distribution" width="500"/>

**Recipe Tags Distribution** - Bar chart showing the distribution of recipe categories and tags.

#### 7. **Advanced Analytics**

<img src="https://github.com/Shre11yeah/Firebase-Based-Recipe-Analytics-Pipeline/blob/main/src/outputs/analytics/charts/recipe_similarity.png" alt="Recipe Similarity Matrix" width="500"/>

**Recipe Similarity Matrix** - Heatmap showing recipe similarities based on ingredients and characteristics.

---

## 🧪 Validation Rules

| Rule | Description |
|------|-------------|
| **Required Fields** | Title, Ingredients, Steps, Difficulty must be present |
| **Positive Values** | Time values and quantities must be ≥ 0 |
| **Difficulty Levels** | Must be one of: `easy`, `medium`, `hard` |
| **Non-empty Arrays** | Ingredients and Steps must contain at least one item |
| **Interaction Types** | Must be one of: `view`, `like`, `rate` |
| **Rating Range** | If present, rating must be between 1-5 |
| **Foreign Keys** | All referenced IDs must exist in parent collections |

---

## 📸 Screenshots

### Firestore Emulator - Recipes Collection
![Recipes Collection](Screenshots/FB-Recipes.jpeg)

### Firestore Emulator - Users Collection
![Users Collection](Screenshots/FB-users.jpeg)

### Firestore Emulator - Interactions Collection
![Interactions Collection](Screenshots/FB-Interactions.jpeg)

---

## 🛠 Technologies Used

- **Firebase Firestore Emulator** - NoSQL document database
- **Python 3.8+** - Primary programming language
- **Pandas** - Data manipulation and analysis
- **Matplotlib/Seaborn** - Data visualization
- **Firebase Admin SDK** - Firestore interaction
- **JSON** - Data interchange format
- **CSV** - Structured data export

### Python Libraries

```
firebase-admin
pandas
matplotlib
seaborn
wordcloud
scikit-learn
python-dotenv
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Made with ❤️ using Firebase and Python**