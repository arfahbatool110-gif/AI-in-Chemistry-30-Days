# ==============================================================================
# DAY 18: Advanced Cheminformatics - Ensemble Regression Modeling
# Description: Training an optimized RandomForestRegressor on the continuous
#              solubility metric (LogS) descriptors using DeepChem featurizers
#              to evaluate mean absolute error metrics.
# ==============================================================================

import warnings
warnings.filterwarnings('ignore')
import numpy as np
import deepchem as dc
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

print("--- Day 18: Training Your First Ensemble Regression Pipeline ---")

# Step 1: Loading standard MoleculeNet physical property continuous data arrays
# Delaney ESOL benchmark handles continuous aqueous solubility predictions
tasks, datasets, transformers = dc.molnet.load_delaney(
    featurizer='ECFP', 
    splitter='random'
)
train_dataset, valid_dataset, test_dataset = datasets

# Step 2: Extracting standard fingerprint feature matrices
X_train, y_train = train_dataset.X, train_dataset.y.ravel()
X_test, y_test = test_dataset.X, test_dataset.y.ravel()

print(f"Total molecular arrays loaded for regression: {len(X_train)} structures")

# Step 3: Initializing the structural ensemble regressor model
reg_model = RandomForestRegressor(n_estimators=100, random_state=42)

# Step 4: Executing optimization fit sequence on molecular properties
reg_model.fit(X_train, y_train)
print("Ensemble Regression training loop finalized successfully.")

# Step 5: Assessing continuous performance predictions on unseen test split
predictions = reg_model.predict(X_test)

# Printing validation tracking parameters to the console
print(f"\n--- AI REGRESSION EVALUATION REPORT ---")
print(f"Mean Absolute Error (MAE): {mean_absolute_error(y_test, predictions):.4f}")
print(f"R-squared (R²) Score:      {r2_score(y_test, predictions):.4f}")
