# Week 4: Classification

This week covers classification fundamentals: Logistic Regression as a first classifier (sigmoid, probability, decision boundaries, thresholds); how to evaluate a classifier honestly (Confusion Matrix, Precision, Recall, F1, Precision/Recall trade-off, ROC/AUC, and why accuracy alone can be misleading); K-Nearest Neighbors as a completely different, equation-free approach; and Decision Trees as a third approach based on sequential yes/no questions. Ends with a direct comparison of all three models on the same dataset, including ROC curves and decision boundaries side by side.

## How to work through this week

1. In `ml-course`, run `git pull` to get this week's files (this repo is read-only for you).
2. In your own repo `ml-course-labs`, create a `week-04/` folder.
3. Copy this week's README and notebooks into it:
   ```
   cp ../ml-course/week-04/README.md      week-04/
   cp ../ml-course/week-04/*.ipynb        week-04/
   ```
4. Open each notebook in order and choose **Restart & Run All**, so the outputs reflect your own execution.
5. Create your own homework notebook applying what this week covered. This is your homework. It isn't handed to you.
6. Commit and push to `ml-course-labs` only and never push to `ml-course`.

## Notebook files

Five notebooks, self-contained, meant to be run in order:

- `01_logistic_regression_intro.ipynb`: Logistic Regression introduced from scratch on a 10-point toy dataset: why linear regression can't do this, the sigmoid, fitting the model, converting probability to a label, and a first, informal look at evaluation.
- `02_logistic_regression.ipynb`: Logistic Regression at full scale on Breast Cancer: train/test split, scaling, the decision boundary visualized, threshold tuning, and evaluation covered in full (confusion matrix, precision/recall/F1, the precision/recall trade-off, ROC/AUC).
- `03_knn.ipynb`: K-Nearest Neighbors worked by hand on a tiny dataset, then at full scale on Breast Cancer: the decision boundary and effect of `k`, choosing `k` by cross-validation, distance metrics, and why scaling matters.
- `04_decision_trees.ipynb`: Decision Trees on the classic Play Tennis dataset (one-hot encoded, fit and visualized), then at full scale on Breast Cancer: seeing the tree on its two strongest features, overfitting without limits, regularization (`max_depth`, `min_samples_split`), and the decision boundary.
- `05_model_comparison.ipynb`: refits all three models on the same dataset and split, then compares metrics, ROC curves, prediction speed, interpretability, and decision boundaries side by side. Closes the week with a summary and exercises.

Notebooks 2 through 5 each load Breast Cancer and split it the same way (`random_state=42`, `stratify=y`), so results are directly comparable across the week, plus the same synthetic 2D `make_moons` dataset for decision-boundary pictures. Imports are made where each tool is first used rather than all at the top, so each notebook doubles as a map of exactly which `sklearn` import a given technique needs.
