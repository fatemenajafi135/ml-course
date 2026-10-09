# Week 7: Unsupervised Learning and Clustering

This week leaves supervised learning behind: no more `y`, just `X`, and the question becomes whether the data forms natural groups on its own. Covers K-Means (centroid intuition, the assign-and-update loop, choosing `k` with the elbow method and silhouette score, and its round-cluster assumption) and DBSCAN (density-based clustering, `eps` and `min_samples`, core/border/noise points, and how it succeeds where K-Means fails on non-round shapes). The first two notebooks work entirely with synthetic data (`make_blobs`, `make_moons`) so the shape of every dataset is known upfront, which makes it possible to see exactly why each algorithm succeeds or fails. The third applies both algorithms to a real dataset, start to finish. Closes with a direct comparison of the two algorithms and why evaluating a clustering, without any ground truth to check against, is harder than evaluating a classifier.

## How to work through this week

1. In `ml-course`, run `git pull` to get this week's files (this repo is read-only for you).
2. In your own repo `ml-course-labs`, create a `week-07/` folder.
3. Copy this week's README and notebooks into it:
   ```
   cp ../ml-course/week-07/README.md      week-07/
   cp ../ml-course/week-07/*.ipynb        week-07/
   cp -r ../ml-course/week-07/assets      week-07/
   ```
4. Open each notebook in order and choose **Restart & Run All**, so the outputs reflect your own execution.
5. Create your own homework notebook applying what this week covered (see below). This is your homework. It isn't handed to you.
6. Commit and push to `ml-course-labs` only and never push to `ml-course`.

## Notebook files

Three notebooks, self-contained, meant to be run in order:

- `01_kmeans.ipynb`: opens with a tiny 8-point toy dataset worked by hand (assign points to the nearest centroid, recompute the centroid, confirmed against `KMeans`), then K-Means at scale on `make_blobs`: fitting and visualizing clusters, choosing `k` with inertia and the elbow method, choosing `k` with silhouette score, K-Means' assumptions (round clusters, similar size, sensitive to feature scale), and a demonstration on `make_moons` where K-Means fails even with the correct `k`.
- `02_dbscan.ipynb`: opens with a tiny 9-point toy dataset worked by hand (classifying each point as core, border, or noise by counting neighbors within `eps`, confirmed against `DBSCAN`), then DBSCAN at scale on the same two-moons dataset K-Means could not handle, the effect of `eps` on the result (too small fragments the data, too large merges clusters together), a direct comparison against K-Means, and why a silhouette score alone can favor the wrong clustering when there is no ground truth to check against.

- `03_penguins_clustering.ipynb`: the worked class example on the real Palmer penguins dataset (`fetch_openml`, downloaded once and cached, so run it once with internet access). The species column is set aside and never fed to the models. Covers EDA, why scaling matters (an unscaled K-Means simply sorts penguins by body mass), choosing `k`, how random initialization changes the result, choosing `eps` with a k-distance plot and an `eps` sweep, K-Means vs DBSCAN side by side, profiling the clusters with columns the model never saw, and finally revealing the true species to check the result (silhouette prefers `k=2`, the real structure is `k=3`).

- `04_clustering_in_practice.ipynb`: the notebook we work through together in class. It starts with 20 hand-made data points (K-Means by hand, elbow, silhouette by hand, DBSCAN core/border/noise by hand, all confirmed against `scikit-learn`), then reuses the same steps on three real datasets: Wine (13 features, where scaling decides everything and DBSCAN struggles), Mall Customers (no labels at all, so we profile the clusters and check stability; the data file is in `assets/`), and Penguins (choosing `k` when the tools disagree, then checking against the hidden species). Ends with a comparison table across all four.

Notebooks 1 and 2 use the same `make_moons` dataset (`n_samples=300, noise=0.08, random_state=42`) so the K-Means failure in notebook 1 and the DBSCAN success in notebook 2 are directly comparable. Imports are made where each tool is first used rather than all at the top, so each notebook doubles as a map of exactly which `sklearn` import a given technique needs.

## Homework

This week's homework uses a real dataset instead of synthetic data: pick one with somewhere between 2 and 5 numeric features (not penguins, that one is the class example). Then:

1. A brief EDA, and a check of feature scale (apply `StandardScaler` if the features differ widely in range).
2. K-Means, choosing `k` with both the elbow method and silhouette score.
3. DBSCAN on the same data.
4. A comparison of the two results, visualized.
5. A short written analysis: what do the clusters you found actually seem to represent?

Create your own notebook `05_hw_clustering.ipynb` in your `ml-course-labs` repo with your solution.
