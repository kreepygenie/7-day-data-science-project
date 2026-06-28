"""
Netflix Titles — Exploratory Data Analysis
Day 1 of #7DaysOfDataScience

Dataset: Netflix Movies & TV Shows (as of 2021), via TidyTuesday
Source: https://github.com/rfordatascience/tidytuesday
"""

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from collections import Counter

NETFLIX_RED = "#E50914"
DARK = "#221f1f"
GREY = "#B3B3B3"
plt.rcParams.update({
    "figure.facecolor": "white",
    "axes.facecolor": "white",
    "axes.edgecolor": GREY,
    "axes.labelcolor": DARK,
    "text.color": DARK,
    "xtick.color": DARK,
    "ytick.color": DARK,
    "font.size": 11,
    "axes.titlesize": 14,
    "axes.titleweight": "bold",
    "axes.spines.top": False,
    "axes.spines.right": False,
})

import os
OUT = os.path.dirname(os.path.abspath(__file__))

df = pd.read_csv(f"{OUT}/netflix_titles.csv")

print("=" * 50)
print("SHAPE:", df.shape)
print("=" * 50)
print(df.dtypes)
print("=" * 50)
print("MISSING VALUES:\n", df.isnull().sum())

df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["date_added"] = pd.to_datetime(df["date_added"].str.strip(), errors="coerce")
df["year_added"] = df["date_added"].dt.year

df["primary_country"] = df["country"].apply(lambda x: x.split(",")[0].strip())

df["duration_num"] = df["duration"].str.extract(r"(\d+)").astype(float)

df["primary_genre"] = df["listed_in"].apply(lambda x: x.split(",")[0].strip())

print("\nCleaned. Sample row:\n", df.iloc[0])

type_counts = df["type"].value_counts()

fig, ax = plt.subplots(figsize=(6, 6))
colors = [NETFLIX_RED, DARK]
wedges, texts, autotexts = ax.pie(
    type_counts.values,
    labels=type_counts.index,
    autopct="%1.1f%%",
    colors=colors,
    startangle=90,
    textprops={"fontsize": 13, "color": "white", "fontweight": "bold"},
    wedgeprops={"edgecolor": "white", "linewidth": 2},
)
for t in texts:
    t.set_color(DARK)
    t.set_fontweight("bold")
ax.set_title("Movies vs TV Shows on Netflix", pad=15)
plt.tight_layout()
plt.savefig(f"{OUT}/chart1_type_distribution.png", dpi=150)
plt.close()

yearly = df["year_added"].value_counts().sort_index()
yearly = yearly[yearly.index >= 2008]

fig, ax = plt.subplots(figsize=(9, 5))
ax.plot(yearly.index, yearly.values, marker="o", color=NETFLIX_RED, linewidth=2.5, markersize=6)
ax.fill_between(yearly.index, yearly.values, color=NETFLIX_RED, alpha=0.08)
ax.set_title("Netflix Content Additions by Year")
ax.set_xlabel("Year Added")
ax.set_ylabel("Titles Added")
ax.grid(axis="y", linestyle="--", alpha=0.4)
plt.tight_layout()
plt.savefig(f"{OUT}/chart2_titles_per_year.png", dpi=150)
plt.close()

top_countries = df[df["primary_country"] != "Unknown"]["primary_country"].value_counts().head(10)

fig, ax = plt.subplots(figsize=(9, 6))
bars = ax.barh(top_countries.index[::-1], top_countries.values[::-1], color=NETFLIX_RED)
ax.set_title("Top 10 Countries by Number of Titles")
ax.set_xlabel("Number of Titles")
for bar in bars:
    w = bar.get_width()
    ax.text(w + 10, bar.get_y() + bar.get_height() / 2, f"{int(w)}", va="center", fontsize=10)
plt.tight_layout()
plt.savefig(f"{OUT}/chart3_top_countries.png", dpi=150)
plt.close()

top_genres = df["primary_genre"].value_counts().head(10)

fig, ax = plt.subplots(figsize=(9, 6))
bars = ax.barh(top_genres.index[::-1], top_genres.values[::-1], color=DARK)
ax.set_title("Top 10 Genres on Netflix")
ax.set_xlabel("Number of Titles")
for bar in bars:
    w = bar.get_width()
    ax.text(w + 8, bar.get_y() + bar.get_height() / 2, f"{int(w)}", va="center", fontsize=10)
plt.tight_layout()
plt.savefig(f"{OUT}/chart4_top_genres.png", dpi=150)
plt.close()

rating_counts = df["rating"].value_counts().head(8)

fig, ax = plt.subplots(figsize=(9, 5))
bars = ax.bar(rating_counts.index, rating_counts.values, color=NETFLIX_RED)
ax.set_title("Most Common Content Ratings")
ax.set_ylabel("Number of Titles")
ax.set_xlabel("Rating")
plt.xticks(rotation=0)
plt.tight_layout()
plt.savefig(f"{OUT}/chart5_rating_distribution.png", dpi=150)
plt.close()

movie_durations = df[df["type"] == "Movie"]["duration_num"].dropna()

fig, ax = plt.subplots(figsize=(9, 5))
ax.hist(movie_durations, bins=30, color=NETFLIX_RED, edgecolor="white")
ax.axvline(movie_durations.median(), color=DARK, linestyle="--", linewidth=2,
           label=f"Median: {movie_durations.median():.0f} min")
ax.set_title("Movie Duration Distribution")
ax.set_xlabel("Duration (minutes)")
ax.set_ylabel("Number of Movies")
ax.legend()
plt.tight_layout()
plt.savefig(f"{OUT}/chart6_movie_duration.png", dpi=150)
plt.close()

print("\n" + "=" * 50)
print("KEY INSIGHTS")
print("=" * 50)
print(f"Total titles: {len(df)}")
print(f"Movies: {type_counts.get('Movie', 0)} ({type_counts.get('Movie', 0)/len(df)*100:.1f}%)")
print(f"TV Shows: {type_counts.get('TV Show', 0)} ({type_counts.get('TV Show', 0)/len(df)*100:.1f}%)")
print(f"Peak content-add year: {yearly.idxmax()} ({yearly.max()} titles)")
print(f"#1 content-producing country: {top_countries.index[0]} ({top_countries.iloc[0]} titles)")
print(f"#1 genre: {top_genres.index[0]} ({top_genres.iloc[0]} titles)")
print(f"Most common rating: {rating_counts.index[0]} ({rating_counts.iloc[0]} titles)")
print(f"Median movie duration: {movie_durations.median():.0f} minutes")

print("\nAll charts saved to:", OUT)
