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


### Week 4: Classification - part I
*Coming soon ...*


### Week 5: Classification - part II
*Coming soon ...*


See each week's own `README.md` for the full breakdown.

## References

Figures adapted from Géron, A. (2025). *Hands-On Machine Learning with
Scikit-Learn and PyTorch* (3rd ed.). O'Reilly.
