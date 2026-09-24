# ==============================================================================
# DAY 11: Data Visualization and Baseline Performance Dashboard
# Description: Generating a clean, production-grade bar chart dashboard using 
#              Matplotlib to visually benchmark and execute a fair evaluation 
#              comparison between Random Forest and SVM classifier scores.
# ==============================================================================

import matplotlib.pyplot as plt

print("--- Day 11: Launching AI Model Evaluation Dashboard ---")

# Step 1: Formulating baseline array names and their respective ROC-AUC metrics
model_names = ['Random Forest (Day 8)', 'Support Vector Machine (Day 10)']
accuracy_scores = [0.9474, 0.8819]

# Step 2: Custom structural dimensions and visual layout design configurations
plt.figure(figsize=(8, 5))
colors = ['#1f77b4', '#ff7f0e']  # Professional standard metric palette mapping
bars = plt.bar(model_names, accuracy_scores, color=colors, width=0.5)

# Step 3: Setting titles, axis indicators, and limits for fair comparison
plt.title("Alzheimer's BACE-1 Predictor: Model Comparison Baseline", fontsize=14, fontweight='bold')
plt.xlabel("Machine Learning Algorithms", fontsize=12)
plt.ylabel("Accuracy Score (ROC-AUC)", fontsize=12)
plt.ylim(0, 1.0)
plt.grid(axis='y', linestyle='--', alpha=0.7)

# Step 4: Iterating data tracking tags above each individual block layer
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2.0, yval + 0.02, f'{yval:.4f}', ha='center', va='bottom', fontsize=11, fontweight='bold')

print("Evaluation dashboard baseline configuration plotted effectively.")
print("Close the pop-up or window instance to terminate script cycle.")

# Final command to display graphical arrays on screen metrics terminal
plt.show()
