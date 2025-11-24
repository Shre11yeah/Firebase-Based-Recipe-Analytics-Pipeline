# # analytics.py
# """
# Loads outputs/csv/*.csv and computes insights:
#  - Most common ingredients
#  - Average preparation time
#  - Difficulty distribution
#  - Correlation between prep time and likes
#  - Most frequently viewed recipes
#  - Ingredients associated with high engagement
#  - Top liked recipes
#  - Average rating per recipe (if ratings exist)
#  - Views per minute (views/total_minutes)
#  - Users with most attempts
# Saves insights to outputs/analytics/insights.md and charts in outputs/analytics/charts/
# """
# import os, pandas as pd
# import matplotlib.pyplot as plt

# CSV_DIR = os.path.join("outputs","csv")
# OUT_DIR = os.path.join("outputs","analytics")
# CHART_DIR = os.path.join(OUT_DIR,"charts")
# os.makedirs(CHART_DIR, exist_ok=True)

# def load():
#     recipes = pd.read_csv(os.path.join(CSV_DIR,"recipe.csv"))
#     ingredients = pd.read_csv(os.path.join(CSV_DIR,"ingredients.csv"))
#     steps = pd.read_csv(os.path.join(CSV_DIR,"steps.csv"))
#     interactions = pd.read_csv(os.path.join(CSV_DIR,"interactions.csv"))
#     return recipes, ingredients, steps, interactions

# def insights():
#     recipes, ingredients, steps, interactions = load()
#     md = []
#     # 1. Most common ingredients
#     top_ings = ingredients['name'].value_counts().head(10)
#     md.append("## 1. Most common ingredients\n")
#     md.append(top_ings.to_markdown() + "\n")

#     # Plot
#     ax = top_ings.sort_values().plot.barh(title="Top Ingredients (count)")
#     fig = ax.get_figure(); fig.tight_layout()
#     fig.savefig(os.path.join(CHART_DIR,"top_ingredients.png"))
#     plt.close(fig)

#     # 2. Average preparation time
#     avg_prep = recipes['prep_minutes'].dropna().astype(float).mean()
#     md.append(f"## 2. Average preparation time (minutes)\n\n{avg_prep:.2f}\n")

#     # 3. Difficulty distribution
#     diff_dist = recipes['difficulty'].value_counts()
#     md.append("## 3. Difficulty distribution\n")
#     md.append(diff_dist.to_markdown() + "\n")
#     ax = diff_dist.plot.pie(autopct="%1.1f%%", title="Difficulty Distribution")
#     ax.get_figure().savefig(os.path.join(CHART_DIR,"difficulty_dist.png"))
#     plt.close()

#     # 4. Correlation between prep time and likes
#     likes = interactions[interactions['type']=="like"].groupby('recipe_id').size().rename("likes")
#     prep = recipes.set_index('recipe_id')['prep_minutes'].astype(float)
#     df_corr = pd.concat([likes, prep], axis=1).dropna()
#     corr = df_corr['likes'].corr(df_corr['prep_minutes']) if not df_corr.empty else None
#     md.append("## 4. Correlation between prep time and likes\n\n")
#     md.append(f"Correlation (Pearson) = {corr}\n\n")

#     # 5. Most frequently viewed recipes
#     views = interactions[interactions['type']=="view"].groupby('recipe_id').size().sort_values(ascending=False).head(10)
#     md.append("## 5. Most frequently viewed recipes\n")
#     md.append(views.to_markdown() + "\n")

#     # 6. Ingredients associated with high engagement (likes/views)
#     engagement = interactions.groupby('recipe_id').size().rename("engagement")
#     recipe_eng = recipes.set_index('recipe_id').join(engagement, how='left').fillna(0)
#     # explode ingredients and compute avg engagement per ingredient
#     ing = ingredients.copy()
#     ing_eng = ing.merge(recipe_eng[['engagement']], left_on='recipe_id', right_index=True)
#     ing_score = ing_eng.groupby('name')['engagement'].mean().sort_values(ascending=False).head(10)
#     md.append("## 6. Ingredients associated with high engagement (avg engagement per recipe containing ingredient)\n")
#     md.append(ing_score.to_markdown() + "\n")

#     # 7. Top liked recipes
#     top_liked = likes.sort_values(ascending=False).head(10)
#     md.append("## 7. Top liked recipes\n")
#     md.append(top_liked.to_markdown() + "\n")

#     # 8. Average rating per recipe
#     if 'rating' in interactions.columns:
#         ratings = interactions.dropna(subset=['rating']).groupby('recipe_id')['rating'].mean().sort_values(ascending=False).head(10)
#         md.append("## 8. Average rating per recipe (top 10)\n")
#         if not ratings.empty:
#             md.append(ratings.to_markdown() + "\n")
#         else:
#             md.append("No rating data available\n")
#     else:
#         md.append("## 8. Average rating per recipe (top 10)\nNo rating column in interactions.\n")

#     # 9. Views per minute (views / total_minutes)
#     recs = recipes.set_index('recipe_id')
#     vpm = views.rename("views").to_frame().join(recs[['total_minutes']], how='left')
#     vpm['views_per_min'] = vpm['views'] / vpm['total_minutes'].replace({0: None})
#     md.append("## 9. Views per minute (per recipe)\n")
#     md.append(vpm.sort_values("views_per_min", ascending=False).head(10).to_markdown() + "\n")

#     # 10. Users with most attempts
#     attempts = interactions[interactions['type']=="attempt"].groupby('user_id').size().sort_values(ascending=False).head(10)
#     md.append("## 10. Users with most attempts\n")
#     md.append(attempts.to_markdown() + "\n")

#     # write insights
#     with open(os.path.join(OUT_DIR,"insights.md"), "w", encoding="utf-8") as f:
#         f.write("\n".join(md))
#     print("Insights written to", os.path.join(OUT_DIR,"insights.md"))

# if __name__ == "__main__":
#     insights()

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

# ---------------------------------------------------
# PREMIUM CHART STYLE SETUP
# ---------------------------------------------------

plt.style.use("ggplot")

plt.rcParams.update({
    "figure.dpi": 180,
    "axes.facecolor": "white",
    "axes.edgecolor": "#333333",
    "axes.labelcolor": "#222222",
    "xtick.color": "#333333",
    "ytick.color": "#333333",
    "grid.color": "#cccccc",
    "axes.titleweight": "bold",
    "axes.titlepad": 15,
    "font.size": 10,
})

# Premium color palette
COLORS = {
    "primary": "#3A7FDB",
    "secondary": "#34A853",
    "tertiary": "#F4B400",
    "danger": "#EA4335",
    "purple": "#9B59B6",
    "cyan": "#17A2B8",
}


# ---------------------------------------------------
# OUTPUT DIRECTORIES
# ---------------------------------------------------

OUTPUT_CHARTS_DIR = "outputs/analytics/charts"
os.makedirs(OUTPUT_CHARTS_DIR, exist_ok=True)


# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

def load_data():
    recipes = pd.read_csv("outputs/csv/recipe.csv")
    ingredients = pd.read_csv("outputs/csv/ingredients.csv")
    interactions = pd.read_csv("outputs/csv/interactions.csv")
    steps = pd.read_csv("outputs/csv/steps.csv")
    return recipes, ingredients, interactions, steps


# ---------------------------------------------------
# 1️⃣ Likes vs Views
# ---------------------------------------------------

def chart_likes_vs_views(interactions):

    views = interactions[interactions["type"] == "view"].groupby("recipe_id").size()
    likes = interactions[interactions["type"] == "like"].groupby("recipe_id").size()

    df = pd.DataFrame({"views": views, "likes": likes}).fillna(0)

    plt.figure(figsize=(7,5))
    plt.scatter(df["views"], df["likes"], color=COLORS["primary"], s=50, alpha=0.7, edgecolor="#1f4e79")
    plt.xlabel("Views")
    plt.ylabel("Likes")
    plt.title("Likes vs Views Correlation")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.savefig(f"{OUTPUT_CHARTS_DIR}/likes_vs_views.png", bbox_inches="tight")
    plt.close()


# ---------------------------------------------------
# 2️⃣ Engagement Score Bar Chart
# ---------------------------------------------------

def chart_engagement_score(interactions):
    engagement = interactions.groupby("recipe_id").size()

    plt.figure(figsize=(10,5))
    engagement.sort_values(ascending=False).plot(
        kind="bar",
        color=COLORS["secondary"]
    )
    plt.title("Recipe Engagement Score")
    plt.xlabel("Recipe ID")
    plt.ylabel("Engagement Score")
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.savefig(f"{OUTPUT_CHARTS_DIR}/engagement_score.png", bbox_inches="tight")
    plt.close()


# ---------------------------------------------------
# 3️⃣ Prep Time vs Likes Scatter Plot
# ---------------------------------------------------

def chart_prep_time_vs_likes(recipes, interactions):

    likes = interactions[interactions["type"] == "like"].groupby("recipe_id").size()
    likes = likes.rename("likes")

    merged = recipes.merge(likes, left_on="recipe_id", right_index=True, how="left")
    merged["likes"] = merged["likes"].fillna(0)

    plt.figure(figsize=(7,5))
    plt.scatter(
        merged["prep_minutes"],
        merged["likes"],
        color=COLORS["tertiary"],
        s=55,
        alpha=0.75,
        edgecolor="#b8860b"
    )

    plt.xlabel("Prep Time (minutes)")
    plt.ylabel("Likes")
    plt.title("Prep Time vs Likes")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.savefig(f"{OUTPUT_CHARTS_DIR}/prep_time_vs_likes.png", bbox_inches="tight")
    plt.close()


# ---------------------------------------------------
# 4️⃣ Ingredient Popularity Heatmap
# ---------------------------------------------------

def chart_ingredient_heatmap(ingredients):
    freq = ingredients["name"].value_counts()

    plt.figure(figsize=(12,2))
    plt.imshow([freq.values], cmap="viridis", aspect="auto")
    plt.xticks(range(len(freq.index)), freq.index, rotation=90)
    plt.yticks([])

    plt.title("Ingredient Popularity Heatmap")
    plt.colorbar(shrink=0.65)
    plt.tight_layout()
    plt.savefig(f"{OUTPUT_CHARTS_DIR}/ingredient_heatmap.png", bbox_inches="tight")
    plt.close()


# ---------------------------------------------------
# 5️⃣ Tags Distribution
# ---------------------------------------------------

def chart_tags_distribution(recipes):

    all_tags = []
    for t in recipes["tags"]:
        tags = t.replace("|", ",").split(",")
        for tg in tags:
            tg = tg.strip()
            if tg:
                all_tags.append(tg)

    tags_series = pd.Series(all_tags)

    plt.figure(figsize=(8,5))
    tags_series.value_counts().plot(kind="bar", color=COLORS["purple"])
    plt.title("Recipe Tags Distribution")
    plt.ylabel("Count")
    plt.grid(axis="y", linestyle="--", alpha=0.4)
    plt.savefig(f"{OUTPUT_CHARTS_DIR}/tags_distribution.png", bbox_inches="tight")
    plt.close()


# ---------------------------------------------------
# 6️⃣ Difficulty vs Average Rating
# ---------------------------------------------------

def chart_difficulty_vs_rating(recipes, interactions):

    if "rating" not in interactions.columns:
        print("⚠️ No rating column found — skipping rating chart.")
        return

    ratings = interactions[interactions["rating"].notna()].groupby("recipe_id")["rating"].mean()

    merged = recipes.merge(ratings, left_on="recipe_id", right_index=True, how="left")

    plt.figure(figsize=(7,5))
    merged.groupby("difficulty")["rating"].mean().plot(
        kind="bar",
        color=COLORS["cyan"]
    )

    plt.title("Difficulty vs Average Rating")
    plt.ylabel("Avg Rating")
    plt.grid(axis="y", alpha=0.3)
    plt.savefig(f"{OUTPUT_CHARTS_DIR}/difficulty_vs_rating.png", bbox_inches="tight")
    plt.close()


# ---------------------------------------------------
# 7️⃣ Most Active Users
# ---------------------------------------------------

def chart_most_active_users(interactions):

    user_freq = interactions["user_id"].value_counts()

    plt.figure(figsize=(9,5))
    user_freq.plot(kind="bar", color=COLORS["danger"])
    plt.title("Most Active Users")
    plt.xlabel("User ID")
    plt.ylabel("Activity Count")
    plt.grid(axis="y", alpha=0.3)
    plt.savefig(f"{OUTPUT_CHARTS_DIR}/active_users.png", bbox_inches="tight")
    plt.close()


# ---------------------------------------------------
# 8️⃣ Hourly Interaction Trend
# ---------------------------------------------------

def chart_hourly_interaction_trend(interactions):

    if "timestamp" not in interactions.columns:
        return

    interactions["hour"] = pd.to_datetime(interactions["timestamp"]).dt.hour
    hourly = interactions.groupby("hour").size()

    plt.figure(figsize=(9,5))
    hourly.plot(kind="line", color=COLORS["primary"], linewidth=2)
    plt.title("Hourly Interaction Trend")
    plt.xlabel("Hour")
    plt.ylabel("Interactions")
    plt.grid(True, alpha=0.4)
    plt.savefig(f"{OUTPUT_CHARTS_DIR}/hourly_trend.png", bbox_inches="tight")
    plt.close()


# ---------------------------------------------------
# 9️⃣ Attempts vs Likes (Stacked)
# ---------------------------------------------------

def chart_attempts_vs_likes(interactions):

    attempts = interactions[interactions["type"] == "attempt"].groupby("recipe_id").size()
    likes = interactions[interactions["type"] == "like"].groupby("recipe_id").size()

    df = pd.DataFrame({"attempts": attempts, "likes": likes}).fillna(0)

    df.plot(
        kind="bar",
        stacked=True,
        figsize=(12,6),
        color=[COLORS["secondary"], COLORS["primary"]]
    )

    plt.title("Attempts vs Likes per Recipe")
    plt.ylabel("Count")
    plt.grid(axis="y", alpha=0.3)
    plt.savefig(f"{OUTPUT_CHARTS_DIR}/attempts_vs_likes.png", bbox_inches="tight")
    plt.close()


# ---------------------------------------------------
# 🔟 Recipe Similarity (Heatmap)
# ---------------------------------------------------

def chart_recipe_similarity(ingredients):

    pivot = ingredients.pivot_table(index="recipe_id", columns="name", aggfunc="size", fill_value=0)
    similarity = pivot.corr()

    plt.figure(figsize=(10,8))
    plt.imshow(similarity, cmap="coolwarm")
    plt.colorbar()
    plt.title("Recipe Similarity Heatmap")
    plt.savefig(f"{OUTPUT_CHARTS_DIR}/recipe_similarity.png", bbox_inches="tight")
    plt.close()


# ---------------------------------------------------
# 1️⃣1️⃣ Word Cloud (if installed)
# ---------------------------------------------------

def chart_ingredient_wordcloud(ingredients):

    try:
        from wordcloud import WordCloud
    except:
        print("WordCloud not installed — skipping.")
        return

    text = " ".join(ingredients["name"])
    wc = WordCloud(background_color="white", colormap="viridis").generate(text)

    plt.figure(figsize=(10,6))
    plt.imshow(wc)
    plt.axis("off")
    plt.savefig(f"{OUTPUT_CHARTS_DIR}/ingredient_wordcloud.png", bbox_inches="tight")
    plt.close()


# ---------------------------------------------------
# MAIN
# ---------------------------------------------------

def main():
    recipes, ingredients, interactions, steps = load_data()

    chart_likes_vs_views(interactions)
    chart_engagement_score(interactions)
    chart_prep_time_vs_likes(recipes, interactions)
    chart_ingredient_heatmap(ingredients)
    chart_tags_distribution(recipes)
    chart_difficulty_vs_rating(recipes, interactions)
    chart_most_active_users(interactions)
    chart_hourly_interaction_trend(interactions)
    chart_attempts_vs_likes(interactions)
    chart_recipe_similarity(ingredients)
    chart_ingredient_wordcloud(ingredients)

    print("\n✅ All premium analytics charts generated successfully!\n")


if __name__ == "__main__":
    main()

