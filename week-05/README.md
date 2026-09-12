# Week 5: Combining Models and Specialized Approaches

This week continues directly from week 4, which ended with Decision Trees: Random Forest (bagging many trees together, feature importance); Ensemble Learning as a full topic in its own right (Bagging vs. Boosting, with real hands-on code for both AdaBoost and Gradient Boosting, not just a mention); Support Vector Machines (maximum margin, support vectors, the kernel trick); and Naive Bayes as a lighter, probabilistic addition alongside SVM. Switches from week 4's Breast Cancer dataset to `load_digits` (handwritten digit images, 10 classes) so every model this week has to handle a real multiclass problem. Ends with a full comparison of all eight models seen across weeks 4–5, refit on this week's dataset.

## How to work through this week

1. In `ml-course`, run `git pull` to get this week's files (this repo is read-only for you).
2. In your own repo `ml-course-labs`, create a `week-05/` folder.
3. Copy this week's README and notebooks into it:
   ```
   cp ../ml-course/week-05/README.md      week-05/
   cp ../ml-course/week-05/*.ipynb        week-05/
   ```
4. Open each notebook in order and choose **Restart & Run All**, so the outputs reflect your own execution.
5. Create your own homework notebook applying what this week covered. This is your homework. It isn't handed to you.
6. Commit and push to `ml-course-labs` only and never push to `ml-course`.

## Notebook files

Five notebooks, self-contained, meant to be run in order:

- `01_random_forest.ipynb`: opens with a tiny 12-point toy dataset worked by hand (bootstrap 3 decision stumps, take a majority vote, then confirm against a real 101-tree forest's `predict_proba`), then dataset EDA (class balance, sample digit images), Random Forest at scale: bagging intuition, effect of `n_estimators`, feature importance visualized as a pixel-importance heatmap, and a boundary comparison against a single Decision Tree.
- `02_ensemble_learning.ipynb`: opens with a tiny 8-point toy dataset worked by hand (AdaBoost's weighted-error and vote-weight formulas, confirmed against `AdaBoostClassifier`'s own attributes), then Ensemble Learning in full at scale: Bagging vs. Boosting, hands-on `AdaBoostClassifier` and `GradientBoostingClassifier` with accuracy tracked across boosting stages, a 3-way boundary comparison against Random Forest, and a mention of the industrial libraries XGBoost/LightGBM/CatBoost.
- `03_svm.ipynb`: opens with a tiny 6-point toy dataset worked by hand (only the support vectors determine the boundary, shown experimentally by moving a non-support point vs. a support vector), then Support Vector Machines at scale: max-margin intuition, linear vs. RBF kernels, why scaling matters.
- `04_naive_bayes.ipynb`: opens with a tiny 8-email spam/ham toy dataset worked by hand (Bayes' theorem, Laplace smoothing, log-probabilities, confirmed against `MultinomialNB`), then a short note on Naive Bayes as a family of models (`MultinomialNB` / `GaussianNB` / `BernoulliNB`) before switching to `GaussianNB` on digits, where the independence assumption visibly costs accuracy on correlated image pixels.
- `05_model_comparison.ipynb`: refits all eight models from weeks 4–5 on this week's dataset and puts them side by side, then closes the week with a summary and exercises, including one revisiting week 4's `load_wine` dataset with all eight models.

Each of the first four notebooks also opens with its own small toy dataset worked by hand, showing how the algorithm actually works mechanically before applying it at scale, the same pattern week 4 used for KNN and Decision Trees. All four then load `load_digits` and split it the same way, so every result is directly comparable across this week's notebooks, plus the same synthetic 2D `make_moons` dataset for decision-boundary pictures. Imports are made where each tool is first used rather than all at the top, so each notebook doubles as a map of exactly which `sklearn` import a given technique needs.
