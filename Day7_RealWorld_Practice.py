# ==============================================================================
# DAY 7: Real-World Data Splitting Practice on Alzheimer's BACE Dataset
# Description: Standard automated split formatting on 1,513 clinical inhibitor 
#              molecules via optimized ECFP featurization metrics.
# ==============================================================================

import warnings
warnings.filterwarnings('ignore')
import deepchem as dc

print("Processing automated data splits on MoleculeNet BACE classification pool.")

# Loading stable baseline arrays via standard ECFP vectors
tasks, datasets, transformers = dc.molnet.load_bace_classification(featurizer='ECFP', splitter='random')
train, valid, test = datasets

print("Optimization array segmentation metrics mapping complete:")
print(f"Final Train Subset Molecule Count: {len(train)}")
print(f"Final Valid Subset Molecule Count: {len(valid)}")
print(f"Final Test Subset Molecule Count:  {len(test)}")
