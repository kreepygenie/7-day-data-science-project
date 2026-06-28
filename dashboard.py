"""
Netflix Content Analytics One page Dashboard
A single combined visual (KPI cards + charts)
"""

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import os

NETFLIX_RED = "#E50914"
DARK = "#221f1f"
GREY = "#8c8c8c"
LIGHT_GREY = "#F5F5F5"

OUT = os.path.dirname(os.path.abspath(__file__))

df = pd.read_csv(f"{OUT}/netflix_titles.csv")
df["country"] = df["country"].fillna("Unknown")
df["primary_country"] = df["country"].apply(lambda x: x.split(",")[0].strip())
df["primary_genre"] = df["listed_in"].apply(lambda x: x.split(",")[0].strip())
df["duration_num"] = df["duration"].str.extract(r"(\d+)").astype(float)

type_counts = df["type"].value_counts()
top_countries = df[df["primary_country"] != "Unknown"]["primary_country"].value_counts().head(6)
top_genres = df["primary_genre"].value_counts().head(6)
rating_counts = df["rating"].value_counts().head(6)
movies_pct = type_counts.get("Movie", 0) / len(df) * 100
median_runtime = df[df["type"] == "Movie"]["duration_num"].median()

plt.rcParams.update({
    "font.size": 11, "axes.edgecolor": "#dddddd",
    "axes.spines.top": False, "axes.spines.right": False,
})
fig = plt.figure(figsize=(16, 10), facecolor="white")

fig.text(0.045, 0.965, "NETFLIX CONTENT ANALYTICS", fontsize=24, fontweight="bold", color=DARK)
fig.text(0.045, 0.935, "Exploratory Data Analysis  ·  Day 1 of 7  ·  7,787 titles analyzed",
         fontsize=12.5, color=GREY)
fig.add_artist(plt.Line2D([0.045, 0.955], [0.915, 0.915], color=NETFLIX_RED, linewidth=2.5))

kpis = [
    ("7,787", "Total Titles"),
    (f"{movies_pct:.0f}%", "Movies Share"),
    ("United States", "Top Country"),
    ("Dramas", "#1 Genre"),
    (f"{median_runtime:.0f} min", "Median Runtime"),
]
n = len(kpis)
margin, gap = 0.045, 0.018
card_w = (0.955 - margin - (n - 1) * gap - margin) / n
for i, (value, label) in enumerate(kpis):
    x = margin + i * (card_w + gap)
    ax = fig.add_axes([x, 0.78, card_w, 0.105])
    ax.set_xlim(0, 1); ax.set_ylim(0, 1)
    ax.axis("off")
    ax.add_patch(FancyBboxPatch((0, 0), 1, 1, boxstyle="round,pad=0,rounding_size=0.08",
                                 transform=ax.transAxes, facecolor=DARK, edgecolor="none"))
    fs = 19 if len(value) <= 7 else 14.5
    ax.text(0.5, 0.62, value, transform=ax.transAxes, ha="center", va="center",
            fontsize=fs, fontweight="bold", color=NETFLIX_RED)
    ax.text(0.5, 0.24, label, transform=ax.transAxes, ha="center", va="center",
            fontsize=10.5, color="white")

gs = fig.add_gridspec(2, 2, left=0.135, right=0.975, top=0.72, bottom=0.045,
                       hspace=0.45, wspace=0.22)

ax1 = fig.add_subplot(gs[0, 0])
wedges, texts, autotexts = ax1.pie(
    type_counts.values, labels=type_counts.index, autopct="%1.0f%%",
    colors=[NETFLIX_RED, DARK], startangle=90,
    textprops={"fontsize": 10, "color": "white", "fontweight": "bold"},
    wedgeprops={"edgecolor": "white", "linewidth": 2},
)
for t in texts:
    t.set_color(DARK); t.set_fontweight("bold"); t.set_fontsize(10)
ax1.set_title("Content Mix: Movies vs TV Shows", fontsize=12.5, fontweight="bold", color=DARK, pad=10)

ax2 = fig.add_subplot(gs[0, 1])
bars = ax2.barh(top_countries.index[::-1], top_countries.values[::-1], color=NETFLIX_RED, height=0.65)
ax2.set_title("Top Content-Producing Countries", fontsize=12.5, fontweight="bold", color=DARK, pad=10)
ax2.tick_params(axis='both', labelsize=10)
for bar in bars:
    w = bar.get_width()
    ax2.text(w + max(top_countries.values)*0.02, bar.get_y() + bar.get_height()/2,
              f"{int(w)}", va="center", fontsize=9.5, color=DARK)
ax2.set_xticks([])

ax3 = fig.add_subplot(gs[1, 0])
bars = ax3.barh(top_genres.index[::-1], top_genres.values[::-1], color=DARK, height=0.65)
ax3.set_title("Top Genres", fontsize=12.5, fontweight="bold", color=DARK, pad=10)
ax3.tick_params(axis='both', labelsize=10)
for bar in bars:
    w = bar.get_width()
    ax3.text(w + max(top_genres.values)*0.02, bar.get_y() + bar.get_height()/2,
              f"{int(w)}", va="center", fontsize=9.5, color=DARK)
ax3.set_xticks([])

ax4 = fig.add_subplot(gs[1, 1])
ax4.bar(rating_counts.index, rating_counts.values, color=NETFLIX_RED, width=0.6)
ax4.set_title("Most Common Content Ratings", fontsize=12.5, fontweight="bold", color=DARK, pad=10)
ax4.tick_params(axis='both', labelsize=10)
ax4.set_yticks([])
for i, v in enumerate(rating_counts.values):
    ax4.text(i, v + max(rating_counts.values)*0.02, f"{int(v)}", ha="center", fontsize=9.5, color=DARK)

fig.text(0.045, 0.012, "Python · pandas · matplotlib", fontsize=9.5, color=GREY)
fig.text(0.955, 0.012, "Dataset: Netflix Movies & TV Shows (Kaggle, via TidyTuesday)",
         fontsize=9.5, color=GREY, ha="right")

plt.savefig(f"{OUT}/dashboard_day1.png", dpi=180, facecolor="white", bbox_inches=None)
plt.close()
print("Dashboard saved.")
