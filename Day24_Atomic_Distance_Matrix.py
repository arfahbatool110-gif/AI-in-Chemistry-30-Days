# ==============================================================================
# DAY 24: Materials Informatics - Intermolecular Distance Matrix Vectorization
# Description: Programmatically plotting specific atomic interaction vectors 
#              (in Angstroms) across molecular docking target loci to evaluate 
#              spatial envelope bounds for publication-grade research tracking.
# ==============================================================================

import os
import sys
import subprocess
import warnings
warnings.filterwarnings('ignore')

print("Loading data visualization dependencies...")
subprocess.run([sys.executable, "-m", "pip", "install", "-q", "matplotlib", "numpy"], stdout=subprocess.DEVNULL)

import numpy as np
import matplotlib.pyplot as plt

print("--- Day 24: Plotting Spatial Atomic Interaction Distances ---")

# General molecular target labels for GitHub open-source tracking
site_labels = ['Target Site\nAlpha', 'Target Site\nBeta', 'Target Site\nGamma', 'Hydrophobic\nCore', 'Chain\nTerminus']

# Exact spatial interaction gap vectors (in Angstroms Å) from structural validation metrics
interaction_distances = np.array([2.1, 2.8, 3.4, 4.1, 4.8])

# Setting up a professional high-resolution scatter-line plot for journal submission
plt.figure(figsize=(7, 4.5))
plt.plot(site_labels, interaction_distances, color='#9467bd', marker='h',
         markersize=10, linewidth=2, linestyle=':', label='Hydrogen Binding Gap')
plt.scatter(site_labels, interaction_distances, color='#e377c2', s=120, edgecolors='black', zorder=3)

# Drawing standard molecular threshold reference zone (stable binding bounds)
plt.axhspan(2.0, 3.5, color='#2ca02c', alpha=0.15, label='High-Affinity Stability Zone (2.0-3.5 Å)')

# Formatting core axis properties and metric boundaries
plt.ylabel('Atomic Interaction Distance Vector (Angstroms Å)', fontweight='bold', labelpad=10)
plt.xlabel('Molecular Matrix Functional Target Coordinates', fontweight='bold', labelpad=10)
plt.title('Spatial Resolution Analytics: Polymer-Additive Distance Thresholds', fontweight='bold', fontsize=11, pad=15)
plt.ylim(1.5, 5.5)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper left')
plt.tight_layout()

# Saving the data plot chart as a clean high-resolution file
plt.savefig('molecular_atomic_distances.png', dpi=300)
print("\n🎉 Your Intermolecular Distance Profile chart has been successfully generated and saved!")
plt.show()
