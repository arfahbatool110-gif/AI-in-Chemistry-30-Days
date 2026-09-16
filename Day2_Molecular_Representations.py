# ==============================================================================
# DAY 2: Molecular Representations (Drawing Paracetamol from SMILES)
# Description: Teaching the computer how a chemical molecule looks using RDKit.
# ==============================================================================

# Step 1: Import RDKit tools for chemistry structure handling
from rdkit import Chem
from rdkit.Chem import Draw

# Step 2: Define the SMILES text for Paracetamol
paracetamol_smiles = "CC(=O)NC1=CC=C(O)C=C1"

# Step 3: Convert the text string into a 2D molecule object in computer memory
molecule = Chem.MolFromSmiles(paracetamol_smiles)

# Step 4: Verify that the molecule is successfully created
if molecule is not None:
    print("Day 2 Success: Paracetamol structure successfully recognized by RDKit!")
else:
    print("Error: Could not read the SMILES string.")

# Note: In Google Colab, you used Draw.MolToImage(molecule) to visualize it.
