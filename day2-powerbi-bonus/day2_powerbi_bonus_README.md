# Day 2 (Bonus) — Customer Segmentation in Power BI

**#7DaysOfDataScience | Day 2 Bonus — Python vs Power BI**

## Dataset
Mall Customers (200 records): CustomerID, Gender, Age, Annual Income (k$),
Spending Score (1-100). Originally from Kaggle (Vijay Choudhary).

## What I did
- Rebuilt Day 2's customer segmentation entirely in Power BI Desktop — no
  Python, no code
- Used Power BI's native "Automatically find clusters" feature on a scatter
  plot of Annual Income vs Spending Score
- Set cluster count to 5, matching the elbow-method result from the Python
  version
- Renamed clusters to the same business-friendly segment names used in the
  Python analysis, for direct comparison
- Built KPI cards (Total Customers, Avg Spending Score, Avg Income) and a
  segment-size bar chart alongside the cluster scatter plot

## Key insights
- **Power BI's built-in clustering reproduced the same 5 segments** found by
  scikit-learn's K-Means in the original Python analysis — same overall
  shape, same outlier groups.
- **"Careful High-Earners" held up identically in both tools**: high income
  (~$88k avg) paired with low spending (score ~17) — confirms that high
  income doesn't predict high spending, validated two different ways.
- **"Average/Standard" was the largest segment in both versions**, by a wide
  margin over every other group.
- **The two smallest segments (Aspirational Spenders and Budget-Conscious)
  swapped rank slightly between tools** — expected, since they're nearly
  tied in size and the two engines use different underlying math (Power
  BI's native clustering vs scikit-learn's K-Means).

## Why this matters
Cross-validating a result across two different tools is a real analytics
skill — trusting a finding because it holds up outside your own code, not
just because the algorithm ran once. Getting the same answer from Power
BI's clustering and Python's K-Means is a stronger signal than either
result alone.

## Files in this folder
- `customer_segmentation.pbix` — full interactive Power BI file (open in
  Power BI Desktop to explore)
- `dashboard_day2_powerbi.png` — exported dashboard screenshot
- `README.md` — this file


