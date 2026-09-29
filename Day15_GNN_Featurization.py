# ==============================================================================
# DAY 15: Advanced Deep Learning - Graph Convolutional Featurization Pipeline
# Description: Extracting 2D molecular graph matrices (Nodes and Edges) from the
#              Alzheimer's BACE benchmark dataset using DeepChem ConvMolFeaturizer
#              to check structural data integrity arrays.
# ==============================================================================

import warnings
warnings.filterwarnings('ignore')
import deepchem as dc

print("--- Day 15: Graph Neural Network (GNN) Feature Pipeline ---")

# Step 1: Initializing the production-grade Convolutional Molecular Featurizer
graph_featurizer = dc.feat.ConvMolFeaturizer()

# Step 2: Loading target data streams using the graphical pipeline processing framework
tasks, datasets, transformers = dc.molnet.load_bace_classification(
    featurizer=graph_featurizer, 
    splitter='random'
)
train_dataset, valid_dataset, test_dataset = datasets

print("GNN Graphical Pipeline execution complete.")

# Step 3: Extracting first training sample object via indexing element [0]
first_molecule_graph = train_dataset.X[0]

# Printing validation verification parameters to the main console terminal
print("\n--- DATA INTEGRITY PROFILE ---")
print(f"Internal Matrix Object Type:        {type(first_molecule_graph).__name__}")
print(f"Total Computed Nodes (Heavy Atoms): {first_molecule_graph.n_atoms}")
print(f"Feature Matrix Vector Dimension:    {first_molecule_graph.get_atom_features().shape}")
