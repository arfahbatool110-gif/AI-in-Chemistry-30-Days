# ==============================================================================
# DAY 12: Deep Learning Foundations - Multi-Layer Perceptron (MLP) for QSAR
# Description: Training an advanced multi-layered Neural Network (MLP) on the
#              Alzheimer's BACE dataset via direct array matrix feeding to safely
#              bypass positional argument weights conflicts on modern software libraries.
# ==============================================================================

import warnings
warnings.filterwarnings('ignore')
import deepchem as dc
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import roc_auc_score

print("--- Day 12: Deep Learning Neural Network Modeling ---")

# Step 1: Loading stable ECFP4 fingerprint matrix streams via MoleculeNet
tasks, datasets, transformers = dc.molnet.load_bace_classification(featurizer='ECFP', splitter='random')
train_dataset, valid_dataset, test_dataset = datasets

# Step 2: Formulating standard multi-layer perceptron neural architecture
model = MLPClassifier(hidden_layer_sizes=(500, 250), max_iter=50, random_state=42)

# Step 3: Executing optimization fit sequence directly on core input/target matrices
print("Initiating deep learning neural layers training sequence...")
model.fit(train_dataset.X, train_dataset.y.ravel())
print("Neural network processing loop finalized successfully.")

# Step 4: Assessing performance metrics on unseen testing entries
test_predictions = model.predict_proba(test_dataset.X)[:, 1]
final_score = roc_auc_score(test_dataset.y, test_predictions)

# Printing validation verification parameters to the main console
print(f"Final Neural Network Test Accuracy Performance Score (ROC-AUC): {final_score:.4f}")
print("Day 8 Baseline Reference - Random Forest Score: 0.9474")
