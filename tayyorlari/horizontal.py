import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Create some sample data
y = np.arange(5)
x = np.random.randint(1, 10, size=5)
colors = ['skyblue', 'salmon', 'lightgreen', 'orchid', 'cornflowerblue']  # Define different colors for each bar

# Create a function to update the bar chart
def update_bar(i):
    ax.clear()
    bars = ax.barh(y, x + i, color=colors)  # Use the colors list to set a different color for each bar and create a horizontal bar chart
    ax.set_xlim(0, 15)
    ax.set_yticks(y)
    ax.set_yticklabels([f'Bar {i+1}' for i in y])
    ax.set_title(f'Horizontal Bar Chart Animation (Frame {i+1})')

# Create a figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, update_bar, frames=10, interval=500, repeat=False)

# Show the animation
plt.show()
