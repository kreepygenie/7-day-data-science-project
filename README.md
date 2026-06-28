# Day 1 — Netflix Titles: Exploratory Data Analysis

**#7DaysOfDataScience | Day 1 of 7**

## Dataset
Netflix Movies & TV Shows catalog (~7,800 titles), sourced via TidyTuesday
(original: Kaggle / Shivam Bansal). Covers titles added up to early 2021.

## What I did
- Cleaned missing `director`, `cast`, `country`, and `date_added` fields
- Parsed dates and durations (minutes for movies, seasons for TV shows)
- Extracted primary country and primary genre from multi-value fields
- Built 6 visualizations covering content mix, growth, geography, genres,
  ratings, and movie length

## Key insights
- **69.1% Movies vs 30.9% TV Shows** — Netflix's catalog is still
  movie-heavy, even though TV Shows drive a lot of the buzz.
- **Content additions peaked in 2019** (2,153 titles that year), then
  dropped sharply — partly a real slowdown, partly because this dataset's
  records taper off after early 2021. Worth flagging when presenting any
  dataset's "recent" trend — always check for a cutoff before reading
  too much into a decline.
- **The US dominates the catalog (2,883 titles)**, but **India is a clear
  #2 (956 titles)** — far ahead of the UK, Canada, and Japan. A strong
  signal of how much weight Netflix puts on Indian content.
- **Dramas (1,384) and Comedies (1,074)** are the top two genres by a wide
  margin over Documentaries and Action & Adventure.
- **TV-MA is the most common rating** (2,863 titles) — the catalog skews
  toward mature audiences more than family content.
- **Median movie length is 98 minutes** — a tight, fairly normal
  distribution, with very few outliers above 3 hours.