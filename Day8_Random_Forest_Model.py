# ==============================================================================
# DAY 8: First AI Baseline Model - Random Forest Classifier for QSAR
# Description: Training a classical Machine Learning model (Random Forest) on the
#              Alzheimer's BACE dataset using DeepChem and evaluating its binary
#              prediction accuracy via ROC-AUC metrics.
# ==============================================================================

import warnings
warnings.filterwarnings('ignore')
import deepchem as dc
from sklearn.ensemble import RandomForestClassifier

print("--- Day 8: Random Forest Predictive Modeling ---")

# Step 1: Loading stable ECFP4 fingerprint matrix streams via MoleculeNet
tasks, datasets, transformers = dc.molnet.load_bace_classification(featurizer='ECFP', splitter='random')
train_dataset, valid_dataset, test_dataset = datasets

# Step 2: Formulating standard Scikit-Learn Random Forest structure with 100 Trees
sklearn_model = RandomForestClassifier(n_estimators=100, random_state=42)
model = dc.models.SklearnModel(sklearn_model)

# Step 3: Executing the optimization fit process on 1,210 training molecules
print("Initiating computer training sequence across processing splits...")
model.fit(train_dataset)
print("Training execution pipeline finalized successfully.")

# Step 4: Assessing performance on 152 unseen testing entries
metric = dc.metrics.Metric(dc.metrics.roc_auc_score)
test_score = model.evaluate(test_dataset, [metric], transformers)

# Printing validation verification parameter to the main terminal console
print(f"Final Model Test Accuracy Performance Score (ROC-AUC): {test_score['roc_auc_score']:.4f}")
