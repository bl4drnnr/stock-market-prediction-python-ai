import matplotlib.pyplot as plt
import numpy as np

# Create data
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.tan(x)
y4 = np.exp(-x)

# Create a 2x2 grid of subplots
fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(10, 12))

# Plot data on each subplot
axes[0, 0].plot(x, y1, label='Sin(x)')
axes[0, 1].plot(x, y2, label='Cos(x)', color='orange')
axes[1, 0].plot(x, y3, label='Tan(x)', color='green')
axes[1, 1].plot(x, y4, label='Exp(-x)', color='red')
axes[2, 0].plot(x, y4, label='Exp(-x)', color='black')
axes[2, 1].plot(x, y4, label='Exp(-x)', color='black')

# Customize layout and labels
fig.suptitle('Multiple Plots in One Figure')
for ax in axes.flatten():
    ax.legend()
    ax.grid(True)

# Adjust layout to prevent clipping of labels
plt.tight_layout()

# Show the figure
plt.show()