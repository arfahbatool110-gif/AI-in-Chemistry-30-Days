# ==============================================================================
# DAY 21: Advanced Materials Informatics - Hyperparameter Convergence Curve
# Description: Programmatically plotting model validation loss trajectories 
#              across variable tree sweeps (n_estimators) using Matplotlib 
#              to lock standard structural saturation thresholds for Paper 2.
# ==============================================================================

import os
import sys
import subprocess
import warnings
warnings.filterwarnings('ignore')

print("Checking environment visualization dependencies...")
# Ensuring clean plotting and mathematical arrays are pre-installed in the loop
subprocess.run([sys.executable, "-m", "pip", "install", "-q", "matplotlib", "numpy"], stdout=subprocess.DEVNULL)

import numpy as np
import matplotlib.pyplot as plt

print("--- Day 21: Plotting Hyperparameter Tuning Convergence Curves ---")

# Standard architectural tuning optimization coordinates matrix
estimators = [10, 50, 100]
mae_scores = [0.4191, 0.3966, 0.3981]

# Creating the high-resolution publication-grade line chart
plt.figure(figsize=(6, 4.5))
plt.plot(estimators, mae_scores, color='#d62728', marker='o', linewidth=2.5, markersize=8, label='Model Error (MAE)')

# Calibration configurations for standard journal papers layout matrices
plt.xlabel('Number of Estimators / Decision Trees (n_estimators)', fontweight='bold', labelpad=10)
plt.ylabel('Validation Mean Absolute Error (MAE)', fontweight='bold', labelpad=10)
plt.title('Hyperparameter Optimization Convergence Curve', fontweight='bold', fontsize=11, pad=15)
plt.xticks(estimators)
plt.grid(True, linestyle=':', alpha=0.6)
plt.legend()
plt.tight_layout()

# Saving the matrix plot as Figure 3 for our article tracking
plt.savefig('hyperparameter_convergence_curve.png', dpi=300)
print("🎉 Your Convergence Curve has been successfully generated and saved!")
plt.show()
