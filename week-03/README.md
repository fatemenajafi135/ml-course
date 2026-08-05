# Week 3: Regression

This week covers simple, multiple, and polynomial linear regression; model evaluation with MAE, RMSE, and R²; and overfitting/underfitting with their standard fixes (regularization and cross-validation).

## How to work through this week

1. In `ml-course`, run `git pull` to get this week's files (this repo is read-only for you).
2. In your own repo `ml-course-labs`, create a `week-03/` folder.
3. Copy this week's README and notebook into it:
   ```
   cp ../ml-course/week-03/README.md          week-03/
   cp ../ml-course/week-03/01_regression.ipynb week-03/
   ```
4. Open the notebook and choose **Restart & Run All**, so the outputs reflect your own execution.
5. Create your own `regression_hw.ipynb` applying what it covered. This is your homework. It isn't handed to you.
6. Commit and push to `ml-course-labs` only and never push to `ml-course`.

## Notebook files

- `01_regression.ipynb`: the complete notebook, explained cell by cell, following the real pipeline in order: a quick look at the data (recap of week 2's EDA, plus a scatter matrix and geographic scatter), train/test split, preparing the data (scaling fit on train only, transformed onto test), simple/multiple/polynomial regression on California Housing and a synthetic dataset, how the weights are found, evaluation metrics (MAE, RMSE, R², plus a residual plot), overfitting and underfitting, learning curves, and the standard fixes (Ridge, Lasso, ElasticNet, cross-validation). Ends with an exercise repeating the pipeline on a different, simpler regression dataset (`load_diabetes`).
