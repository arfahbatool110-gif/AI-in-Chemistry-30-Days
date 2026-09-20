# ==============================================================================
# DAY 6: Train / Valid / Test Data Splits
# Description: Loading the Delaney solubility dataset using DeepChem and splitting
#              the chemical matrices into Training, Validation, and Test sets 
#              to prevent overfitting during AI model evaluation.
# ==============================================================================

import warnings
warnings.filterwarnings('ignore')
import deepchem as dc

print("--- Day 6: Train / Valid / Test Data Splitting ---")

# Automatically loading and splitting dataset arrays via DeepChem MoleculeNet
tasks, datasets, transformers = dc.molnet.load_delaney(featurizer='ECFP')
train_dataset, valid_dataset, test_dataset = datasets

print("Dataset successfully partitioned into target arrays:")
print(f"Training Subset Entry Count:   {len(train_dataset)}")
print(f"Validation Subset Entry Count: {len(valid_dataset)}")
print(f"Testing Subset Entry Count:    {len(test_dataset)}")
