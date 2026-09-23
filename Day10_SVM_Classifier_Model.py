# ==============================================================================
# DAY 10: Second AI Baseline Model - Support Vector Machine (SVM) Classifier
# Description: Training a Support Vector Machine (SVM) Classifier on the 
#              Alzheimer's BACE dataset via DeepChem and executing a fair baseline
#              comparison against the Day 8 Random Forest metrics.
# ==============================================================================

import warnings
warnings.filterwarnings('ignore')
import deepchem as dc
from sklearn.svm import SVC

print("--- Day 10: Support Vector Machine (SVM) Modeling ---")

# Step 1: Loading baseline ECFP4 fingerprint matrix streams via MoleculeNet
tasks, datasets, transformers = dc.molnet.load_bace_classification(featurizer='ECFP', splitter='random')
train_dataset, valid_dataset, test_dataset = datasets

# Step 2: Formulating standard Scikit-Learn SVM structure with RBF Kernel
sklearn_svm = SVC(kernel='rbf', probability=True, random_state=42)
model = dc.models.SklearnModel(sklearn_svm)

# Step 3: Executing optimization fit sequence on 1,210 training molecules
print("Initiating computer SVM training sequence across processing splits...")
model.fit(train_dataset)
print("SVM Training execution pipeline finalized successfully.")

# Step 4: Assessing performance on 152 unseen testing entries
metric = dc.metrics.Metric(dc.metrics.roc_auc_score)
test_score = model.evaluate(test_dataset, [metric], transformers)

# Printing validation parameters for model evaluation benchmarking
print(f"Final SVM Model Test Accuracy Performance Score (ROC-AUC): {test_score['roc_auc_score']:.4f}")
print("Day 8 Baseline Reference - Random Forest Score: 0.9474")
