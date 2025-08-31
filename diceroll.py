import numpy as np
import matplotlib.pyplot as plt
from collections import Counter

# Number of simulations
n_rolls = 10000

# Roll two dice using numpy (part of scipy ecosystem)
dice1 = np.random.randint(1, 7, n_rolls)
dice2 = np.random.randint(1, 7, n_rolls)
sums = dice1 + dice2

# Count outcomes
counts = Counter(sums)
percentages = {i: (counts[i] / n_rolls) * 100 for i in range(2, 13)}

# Print results
print("Dice Roll Outcome Probabilities:")
for i in range(2, 13):
    print(f"Sum {i}: {percentages[i]:.2f}%")

# Plot results
plt.bar(percentages.keys(), percentages.values(), color='skyblue', edgecolor='black')
plt.xlabel("Sum of Two Dice")
plt.ylabel("Percentage (%)")
plt.title("Dice Roll Simulation (10,000 rolls)")
plt.xticks(range(2, 13))
plt.grid(axis='y', linestyle='--', alpha=0.6)
plt.show()
