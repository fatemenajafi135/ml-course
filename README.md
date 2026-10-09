# ml-course
A 10-week ML course

## About this repo

`ml-course` hosts both the slides and the per-week code for the course. It's
public and **read-only for students** — `git pull` it each week, but never
push to it.

Each student keeps their own homework and notebooks in a separate repo,
`ml-course-labs`. Every week's `README.md` here says exactly what to copy
over and how.

## Weeks

### [Week 0: Course Introduction](week-00/)
- What machine learning is
- Why learn machine learning
- ML as the solution

### [Week 1: Introduction to Machine Learning](week-01/)
- The ML project lifecycle: problem definition, data collection, data prep, training, evaluation, deployment
- Data types: tabular, text, image, audio, video
- Types of ML systems: supervised, unsupervised, and reinforcement learning
- Tools of the course: Python, Jupyter Notebook, VS Code, Miniconda, Google Colab
- Homework: a pure-Python library management system and a student-scores exercise

### [Week 2: NumPy, pandas, matplotlib, and EDA](week-02/)
- **NumPy**: creating arrays, array anatomy, indexing/slicing/views, reshaping/joining/splitting, iterating, vectorization and broadcasting, aggregations/sorting/searching, linear algebra essentials, random number generation, inserting/appending/deleting elements, performance
- **pandas**: Series and DataFrames, inspecting a DataFrame, selecting data (`loc`/`iloc`/boolean masks), adding/transforming/dropping columns, sorting/counting/summarizing, handling missing data, `groupby`, combining DataFrames (`concat`/`merge`), reshaping (pivot/melt), pandas in the ML stack
- **matplotlib**: first plots, the Figure/Axes object model, anatomy of a figure, line/scatter plots, bar charts/histograms, styling, subplot grids, saving/displaying figures, matplotlib in the ML stack
- **EDA & data cleaning**: first look at a dataset (shape, dtypes, summary stats), univariate and bivariate exploration, missing values, duplicates, outliers, and feature scaling (`StandardScaler` vs `MinMaxScaler`)

### [Week 3: Regression](week-03/)
- Simple, multiple, and polynomial linear regression on California Housing (plus a synthetic dataset), and how the weights are found
- Evaluation metrics: MAE, RMSE, R², and residual plots
- Overfitting and underfitting, learning curves, and the standard fixes: Ridge, Lasso, ElasticNet, and cross-validation

### [Week 4: Classification](week-04/)
- Logistic Regression (sigmoid, probability, decision boundaries, thresholds)
- Evaluation metrics: Confusion Matrix, Precision, Recall, F1, Precision/Recall trade-off, ROC/AUC
- K-Nearest Neighbors as an equation-free classifier
- Decision Trees and sequential yes/no questions
- Comparing Logistic Regression, KNN, and Decision Trees

### [Week 5: Classification part II - Combining Models and Specialized Approaches](week-05/)
- Random Forest: bagging many trees together, effect of `n_estimators`, feature importance
- Ensemble Learning as a full topic: Bagging vs. Boosting, with hands-on AdaBoost and Gradient Boosting
- Support Vector Machines: maximum margin, support vectors, the kernel trick
- Naive Bayes: Bayes' theorem, the independence assumption, a worked spam-filter example
- Final comparison of all eight models seen across weeks 4–5

### [Week 6: Feature Engineering, Pipelines, and Model Selection](week-06/)
- Handling missing values with imputation strategies
- Feature scaling: `StandardScaler` vs `MinMaxScaler`
- Categorical encoding: one-hot, ordinal, and target encoding
- Feature engineering: creating, selecting, and transforming features
- Pipelines (`Pipeline` and `ColumnTransformer`) to organize workflows and prevent data leakage
- Model evaluation: train/test split, cross-validation, validation curves
- Hyperparameter tuning: grid search and random search
- End-to-end workflow on real datasets (Titanic)

### [Week 7: Unsupervised Learning and Clustering](week-07/)
- **K-Means**: centroid-based clustering, the assign-and-update algorithm, choosing `k` with elbow method and silhouette score, handling non-spherical clusters
- **DBSCAN**: density-based clustering, `eps` and `min_samples` parameters, core/border/noise points, success on non-round shapes
- Real dataset application: Palmer Penguins with EDA, scaling, and comparison against ground truth
- Clustering evaluation metrics without ground truth (silhouette score, inertia)
- Comparison of K-Means vs DBSCAN and why unsupervised evaluation is harder

See each week's own `README.md` for the full breakdown.

## References

Figures adapted from Géron, A. (2025). *Hands-On Machine Learning with
Scikit-Learn and PyTorch* (3rd ed.). O'Reilly.
