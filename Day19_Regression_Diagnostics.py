# ==============================================================================
# DAY 19: Advanced Materials Informatics - Diagnostic Scatter Visualisation
# Description: Training an ensemble RandomForestRegressor on Delaney LogS arrays
#              via DeepChem and plotting actual vs predicted values along an 
#              ideal 45-degree identity reference diagonal line.
# ==============================================================================

import os
import sys
import subprocess
import warnings
warnings.filterwarnings('ignore')

print("Checking data visualization dependencies...")
# Ensuring clean plotting libraries are pre-installed in the current environment
subprocess.run([sys.executable, "-m", "pip", "install", "-q", "matplotlib", "numpy", "deepchem", "scikit-learn"], stdout=subprocess.DEVNULL)

import numpy as np
import matplotlib.pyplot as plt
import deepchem as dc
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

print("--- Day 19: Generating Regression Scatter Plot Diagnostics ---")

# Step 1: Loading standard Delaney continuous molecular solubility dataset
tasks, datasets, transformers = dc.molnet.load_delaney(featurizer='ECFP', splitter='random')
train_dataset, valid_dataset, test_dataset = datasets

# Step 2: Mapping chemical fingerprints into training matrices
X_train, y_train = train_dataset.X, train_dataset.y.ravel()
X_test, y_test = test_dataset.X, test_dataset.y.ravel()

# Step 3: Initializing and fitting the structural ensemble regressor engine
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)
print("Regression Model training loop finalized successfully.")

# Step 4: Extracting predictions profile on unseen testing graphs
predictions = model.predict(X_test)
mae = mean_absolute_error(y_test, predictions)

# Step 5: Generating the professional model validation scatter chart
plt.figure(figsize=(6, 5))
plt.scatter(y_test, predictions, color='#1f77b4', alpha=0.6, edgecolors='black', s=50, label='Computed Predictions')

# Drawing the 100% Ideal Prediction Diagonal Line
line_range = np.linspace(min(y_test)-0.5, max(y_test)+0.5, 100)
plt.plot(line_range, line_range, color='#d62728', linestyle='--', linewidth=2, label='100% Ideal Reference')

# Setting up structural axis boundaries and text parameters
plt.xlabel('Actual Experimental Values (Target Matrix)', fontweight='bold', labelpad=10)
plt.ylabel('AI Computed Predictions (Model Output)', fontweight='bold', labelpad=10)
plt.title(f'Materials Informatics Model Validation (MAE: {mae:.4f})', fontweight='bold', fontsize=11, pad=15)
plt.grid(True, linestyle=':', alpha=0.5)
plt.legend()
plt.tight_layout()

# Saving the matrix plot as a high-resolution file for publication tracking
plt.savefig('regression_diagnostic_scatter.png', dpi=300)
print("🎉 Diagnostic chart has been generated and saved as 'regression_diagnostic_scatter.png'!")
