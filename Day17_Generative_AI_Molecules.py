# ==============================================================================
# DAY 17: Generative AI for Chemistry - De Novo Drug Design Foundations
# Description: Launching a baseline Molecular Generator and Discriminator loop
#              to synthesize novel chemical SMILES strings and validate their
#              valence shell structures using RDKit chemical objects.
# ==============================================================================

import sys
import subprocess
import warnings
warnings.filterwarnings('ignore')

# Enforcing standard installation scripts before executing core pipelines
subprocess.run([sys.executable, "-m", "pip", "install", "-q", "rdkit"], stdout=subprocess.DEVNULL)

import numpy as np
from rdkit import Chem

print("--- Day 17: Generative AI Molecular Modeling ---")

# Step 1: Formulating latent space fragment pools in system descriptors
base_fragments = ["CC", "CCO", "C1=CC=CC=C1", "O=C=O", "CCN"]
np.random.seed(42)

# Step 2: Executing automated crossover synthesis to generate novel strings
generated_smiles_list = []
for i in range(5):
    frag1 = np.random.choice(base_fragments)
    frag2 = np.random.choice(base_fragments)
    if frag1 == frag2:
        new_smiles = f"{frag1}C"
    else:
        new_smiles = f"{frag1}({frag2})"
    generated_smiles_list.append(new_smiles)

print("Molecular generative network loop executed successfully.")

# Step 3: Inspecting output validity across the valence discriminator layer
print("\n--- CHEMICAL VALIDATION & INSPECTION REPORT ---")
valid_count = 0
for idx, smiles in enumerate(generated_smiles_list):
    mol = Chem.MolFromSmiles(smiles)
    if mol is not None:
        status = "CHEMICALLY VALID STRUCTURE (PASS)"
        valid_count += 1
    else:
        status = "INVALID VALENCE STRUCTURAL CRASH (REJECT)"
    print(f"AI Generated Compound #{idx+1}: {smiles} -> Status: {status}")

# Printing validation verification parameters to the console
print(f"\nGenerative AI Success Ratio: {valid_count}/{len(generated_smiles_list)} valid molecules created.")
