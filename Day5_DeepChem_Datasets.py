# ==============================================================================
# DAY 5: Data Handling and Dataset Objects in DeepChem
# Description: Learning how to pack raw molecular feature vectors and chemical 
#              labels into structured DeepChem NumpyDataset objects for AI models.
# ==============================================================================

import numpy as np
import deepchem as dc

print("--- Day 5: DeepChem Data Handling ---")

# Formulating numerical array shapes for 3 theoretical chemical matrices
fake_fingerprints = np.array([
    [1, 0, 1, 0, 1],  # Molecule A property array
    [0, 1, 1, 0, 0],  # Molecule B property array
    [1, 1, 0, 1, 1]   # Molecule C property array
])

# Defining binary target outcomes (e.g., 1 = active inhibitor, 0 = inactive)
chemical_labels = np.array([1, 0, 1])

# Converting basic matrices into deep learning compatible objects
dataset = dc.data.NumpyDataset(X=fake_fingerprints, y=chemical_labels)

print("DeepChem Dataset configuration finalized effectively.")
print("Dataset Matrix Shape (Samples, Features):", dataset.X.shape)
