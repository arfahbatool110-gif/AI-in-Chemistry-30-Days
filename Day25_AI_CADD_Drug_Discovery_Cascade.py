# ==============================================================================
# DAY 25: AI in Drug Discovery - AI-Based Cascades for CADD
# Description: Modeling the foundational validation gate of a Computer-Aided 
#              Drug Design (CADD) cascade by tracking binding calibration indices.
# ==============================================================================

import os
import sys
import subprocess
import warnings
warnings.filterwarnings('ignore')

print("Initializing AI CADD Drug Discovery Cascade Components...")
subprocess.run([sys.executable, "-m", "pip", "install", "-q", "matplotlib", "numpy"], stdout=subprocess.DEVNULL)

import numpy as np
import matplotlib.pyplot as plt

print("--- Day 25: Executing CADD Virtual Screening Cascade Layer 1 ---")

# Cascade Matrix coordinates processing
experimental_cadd_scores = np.array([-5.2, -7.1, -8.5, -9.2, -10.5])
ai_computed_cadd_scores = np.array([-5.4, -6.9, -8.7, -9.0, -10.8])

# Generating the core cascade validation parity plot
plt.figure(figsize=(6, 5))
plt.scatter(experimental_cadd_scores, ai_computed_cadd_scores, color='#17becf', s=100, edgecolors='black', alpha=0.85, label='Screened Compounds')

line_range = np.linspace(min(experimental_cadd_scores)-0.5, max(experimental_cadd_scores)+0.5, 100)
plt.plot(line_range, line_range, color='#ff7f0e', linestyle='--', linewidth=2, label='Ideal CADD Reference Line')

plt.xlabel('Experimental Ground Truth \u0394G (kcal/mol)', fontweight='bold', labelpad=10)
plt.ylabel('AI Computed CADD Predictions (kcal/mol)', fontweight='bold', labelpad=10)
plt.title('AI-Based CADD Cascade: Validation Metrics', fontweight='bold', fontsize=11, pad=15)
plt.grid(True, linestyle=':', alpha=0.5)
plt.legend(loc='upper left')
plt.tight_layout()

# Saving asset under core structural title names
plt.savefig('ai_cadd_cascade_validation.png', dpi=300)
print("\n🎉 Your CADD Cascade Validation Plot has been successfully generated and saved!")
