# ==============================================================================
# DAY 4: Molecular Fingerprints & Tanimoto Similarity Score
# Description: Converting molecular structures into mathematical numbers (bits)
#              to calculate the chemical similarity between two drugs.
# ==============================================================================

# Step 1: Import RDKit tools for fingerprinting and similarity assessment
from rdkit import Chem
from rdkit.Chem import AllChem
from rdkit import DataStructs

print("--- Day 4: Molecular Fingerprints & Similarity ---")

# Step 2: Define SMILES formulas for Ethanol (Alcohol) and Caffeine (Coffee)
ethanol_smiles = "CCO"
caffeine_smiles = "CN1C=NC2=C1C(=O)N(C(=O)N2C)C"

# Step 3: Generate molecule objects in computer memory from SMILES strings
mol_a = Chem.MolFromSmiles(ethanol_smiles)
mol_b = Chem.MolFromSmiles(caffeine_smiles)

# Step 4: Extract Morgan Fingerprints (ECFP4)
# We convert structures into a vector of 2048 bits (0s and 1s) with a radius of 2
fp_a = AllChem.GetMorganFingerprintAsBitVect(mol_a, radius=2, nBits=2048)
fp_b = AllChem.GetMorganFingerprintAsBitVect(mol_b, radius=2, nBits=2048)

# Step 5: Compute Tanimoto Similarity Score (Returns value between 0.0 and 1.0)
similarity_score = DataStructs.TanimotoSimilarity(fp_a, fp_b)

# Print the final result to verify calculation accuracy
print(f"Similarity score between Ethanol and Caffeine: {similarity_score:.4f}")
