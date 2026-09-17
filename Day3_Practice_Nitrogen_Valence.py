# ==============================================================================
# DAY 3 PRACTICE: Custom Valence Error Checking for Nitrogen
# Description: Testing if RDKit can catch invalid bonds for Nitrogen (5 bonds).
# ==============================================================================

from rdkit import Chem

print("--- Day 3 Practice: Nitrogen Error Checking ---")

# Nitrogen with 5 bonds (Chemically invalid)
galat_nitrogen_smiles = "N(C)(C)(C)(C)(C)" 

try:
    # Attempting to read and sanitize the molecule
    mol_nitrogen = Chem.MolFromSmiles(galat_nitrogen_smiles, sanitize=True)
except Exception as e:
    # If an error occurs, set molecule to None
    mol_nitrogen = None

# Verify if RDKit successfully caught the error
print("Did RDKit catch the Nitrogen valence error?", mol_nitrogen is None)
