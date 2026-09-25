import pandas as pd
import matplotlib.pyplot as plt

# Load the evaluation results
df = pd.read_csv("analysis/results.csv")

# Create a readable label for each condition
df["label"] = df["condition_type"] + ": " + df["condition"].astype(str)

# Plot Power Expansion scores
plt.figure(figsize=(10, 6))
plt.bar(df["label"], df["power_expansion"])

plt.title("Power Expansion by Experimental Condition")
plt.xlabel("Condition")
plt.ylabel("Power Expansion Score")
plt.ylim(0, 5)

plt.xticks(rotation=45, ha="right")
plt.tight_layout()

plt.savefig("analysis/power_expansion.png", dpi=300)
plt.show()
