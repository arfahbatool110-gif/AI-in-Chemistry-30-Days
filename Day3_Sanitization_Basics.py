# ==============================================================================
# DAY 3: Chemistry Rule Checking (Sanitization)
# Description: Teaching the computer how to detect invalid chemical formulas.
# ==============================================================================

# Step 1: Import core RDKit tool
from rdkit import Chem

print("--- Day 3: Chemical Validation (Sanitization) ---")

# 1. Testing a VALID molecule: Ethanol (Alcohol)
valid_smiles = "CCO" 
mol_valid = Chem.MolFromSmiles(valid_smiles)
print("Is Ethanol chemically valid?", mol_valid is not None)  # Will print True

# 2. Testing an INVALID molecule: Carbon with 5 bonds (Chemistry rule error)
invalid_smiles = "C(F)(Cl)(Br)(I)(C)" 
try:
    # RDKit will automatically sanitize and catch the valence error
    mol_invalid = Chem.MolFromSmiles(invalid_smiles, sanitize=True)
except Exception as e:
    mol_invalid = None

print("Did RDKit catch the invalid molecule?", mol_invalid is None)  # Will print True
