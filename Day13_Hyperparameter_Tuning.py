# ==============================================================================
# DAY 13: Model Optimization - Hyperparameter Tuning via GridSearchCV
# Description: Tuning and optimizing the Random Forest baseline classifier on 
#              the Alzheimer's BACE dataset using 3-fold cross-validation
#              parameters on Scikit-Learn matrices.
# ==============================================================================

import warnings
warnings.filterwarnings('ignore')
import deepchem as dc
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV

print("--- Day 13: Hyperparameter Tuning Grid Search ---")

# Step 1: Loading stable ECFP4 fingerprint matrix streams via MoleculeNet
tasks, datasets, transformers = dc.molnet.load_bace_classification(featurizer='ECFP', splitter='random')
train_dataset, valid_dataset, test_dataset = datasets

# Step 2: Defining parameter grid dictionary matrix (Explicit Fixed List)
param_grid = {
    'n_estimators':,
    'max_depth': [None, 10]
}

# Step 3: Setting up the cross-validation optimization pipeline
base_rf = RandomForestClassifier(random_state=42)
grid_search = GridSearchCV(estimator=base_rf, param_grid=param_grid, cv=3, scoring='roc_auc', n_jobs=-1)

# Step 4: Executing optimization fit directly on core input arrays
print("Executing automated tuning iterations across grid layers...")
grid_search.fit(train_dataset.X, train_dataset.y.ravel())
print("Hyperparameter tuning execution completed successfully.")

# Printing validation verification parameters to the main console
print("\n--- FINAL TUNING REPORT ---")
print(f"Optimized Parameters Selected: {grid_search.best_params_}")
print(f"Top Validation Score Achieved: {grid_search.best_score_:.4f}")
