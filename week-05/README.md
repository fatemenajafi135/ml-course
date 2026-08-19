# Week 5: Combining Models and Specialized Approaches

This week continues directly from week 4, which ended with Decision Trees: Random Forest (bagging many trees together, feature importance); Ensemble Learning as a full topic in its own right (Bagging vs. Boosting, with real hands-on code for both AdaBoost and Gradient Boosting, not just a mention); Support Vector Machines (maximum margin, support vectors, the kernel trick); and Naive Bayes as a lighter, probabilistic addition alongside SVM. Ends with a full comparison of all eight models seen across weeks 4–5 on the same dataset.

## How to work through this week

1. In `ml-course`, run `git pull` to get this week's files (this repo is read-only for you).
2. In your own repo `ml-course-labs`, create a `week-05/` folder.
3. Copy this week's README and notebook into it:
   ```
   cp ../ml-course/week-05/README.md                     week-05/
   cp ../ml-course/week-05/01_ensembles_and_beyond.ipynb  week-05/
   ```
4. Open the notebook and choose **Restart & Run All**, so the outputs reflect your own execution.
5. Create your own `ensembles_and_beyond_hw.ipynb` applying what it covered. This is your homework. It isn't handed to you.
6. Commit and push to `ml-course-labs` only and never push to `ml-course`.

## Notebook files

- `01_ensembles_and_beyond.ipynb`: the complete notebook, explained cell by cell. Reuses the exact same `Breast Cancer Wisconsin` dataset and train/test split as week 4, so every result here is directly comparable to last week's Logistic Regression, KNN, and Decision Tree numbers, plus the same synthetic 2D dataset for decision-boundary pictures. Covers: Random Forest (bagging intuition, effect of `n_estimators`, feature importance, boundary comparison against a single tree), Ensemble Learning in full (Bagging vs. Boosting, hands-on `AdaBoostClassifier` and `GradientBoostingClassifier` with accuracy tracked across boosting stages, a 3-way boundary comparison against Random Forest, and a mention of the industrial libraries XGBoost/LightGBM/CatBoost), Support Vector Machines (max-margin intuition with support vectors, linear vs. RBF kernels, why scaling matters), Naive Bayes (Bayes' theorem intuition, the independence assumption, a callback to week 4's spam-detection example), and a final side-by-side comparison of all eight models from weeks 4–5. Ends with an exercise revisiting week 4's `load_wine` multiclass dataset with all eight models.
