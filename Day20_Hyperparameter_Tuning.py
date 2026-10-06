# ==============================================================================
# DAY 20: Advanced Cheminformatics - Regressor Hyperparameter Optimization
# Description: Deploying systematic iteration loops across variable tree density 
#              sweeps (n_estimators) using DeepChem loaders to minimize the
#              global Mean Absolute Error (MAE) loss function.
# ==============================================================================

import os
import sys
import subprocess
import warnings
warnings.filterwarnings('ignore')

print("Checking environment tuning dependencies...")
# Ensuring safe optimization components are pre-installed in the current container
subprocess.run([sys.executable, "-m", "pip", "install", "-q", "deepchem", "scikit-learn", "numpy"], stdout=subprocess.DEVNULL)

import numpy as np
import deepchem as dc
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

print("--- Day 20: Executing Regressor Hyperparameter Optimization Loops ---")

# Step 1: Loading standard Delaney continuous molecular solubility datasets
tasks, datasets, transformers = dc.molnet.load_delaney(featurizer='ECFP', splitter='random')
train_dataset, valid_dataset, test_dataset = datasets

# Step 2: Extracting feature descriptor matrices from testing grids
X_train, y_train = train_dataset.X, train_dataset.y.ravel()
X_test, y_test = test_dataset.X, test_dataset.y.ravel()

# Step 3: Setting up the optimization structural variance sweep arrays
estimator_options = [10, 50, 100]

print("Hyperparameter arrays sweeping started background configurations...")
for trees in estimator_options:
    # Adjusting core ensemble parameters dynamically across each iteration
    model = RandomForestRegressor(n_estimators=trees, random_state=42)
    model.fit(X_train, y_train)
    
    # Evaluating validation tracking scores on unseen structural matrices
    predictions = model.predict(X_test)
    error_mae = mean_absolute_error(y_test, predictions)
    
    print(f"Configuring Configuration: [n_estimators={trees:3d}] -> Resulting Mean Absolute Error (MAE): {error_mae:.4f}")

print("\n🎉 Hyperparameter tuning loop completed successfully!")
