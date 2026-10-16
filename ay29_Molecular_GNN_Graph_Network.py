# ==============================================================================
# DAY 29: AI in Drug Discovery - Graph Neural Networks (GNN) & Molecular Graphs
# Description: Programmatically simulating a molecular graph architecture by 
#              mapping atomic nodes and chemical bonding vectors for GNN learning.
# ==============================================================================

import os
import sys
import subprocess
import warnings
warnings.filterwarnings('ignore')

print("Loading Graph Neural Networks modeling wrappers...")
subprocess.run([sys.executable, "-m", "pip", "install", "-q", "matplotlib", "numpy"], stdout=subprocess.DEVNULL)

import numpy as np
import matplotlib.pyplot as plt

print("--- Day 29: Executing Molecular Graph Connectivity Profiling ---")

# Defining atomic nodes configuration network variables (e.g., Target atoms indices)
atomic_centers = ['Atom C1', 'Atom C2', 'Atom O3', 'Atom N4', 'Atom S5']
bonding_vectors_density = np.array([3.8, 4.2, 5.9, 4.8, 6.4]) # Interconnected weights indices

plt.figure(figsize=(6.5, 4.5))

# Generating a high-resolution publication-grade connectivity polar visual representation
angles = np.linspace(0, 2 * np.pi, len(atomic_centers), endpoint=False).tolist()
bonding_metrics = np.concatenate((bonding_vectors_density, [bonding_vectors_density[0]]))
angles += angles[:1]

ax = plt.subplot(111, polar=True)
ax.plot(angles, bonding_metrics, color='#2ca02c', linewidth=2, linestyle='-', marker='o', markersize=8)
ax.fill(angles, bonding_metrics, color='#2ca02c', alpha=0.25)

plt.xticks(angles[:-1], atomic_centers, fontweight='semibold')
ax.set_yticklabels([]) # Hiding default radial metrics grid numbers for clean journal view
plt.title('Molecular Graph Configuration Vector for GNN Training', fontweight='bold', fontsize=11, pad=15)
plt.tight_layout()

# Saving the final Figure 10 for our paper
plt.savefig('molecular_gnn_graph_network.png', dpi=300)
print("\n🎉 Your Molecular Graph Network visual has been successfully saved as 'molecular_gnn_graph_network.png'!")
plt.show()
