import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Sample data for different years
years = [2010, 2011, 2012, 2013, 2014]
values = np.random.randint(1, 10, size=(5, 5))  # Random values for each year

# Create a function to update the bar chart for each year
def update_bar(i):
    ax.clear()
    sorted_indices = np.argsort(values[i])  # Sort the values for the current year
    sorted_values = values[i][sorted_indices]  # Sort the values
    y = np.arange(len(sorted_values))  # Create y positions based on the number of bars
    bars = ax.barh(y, sorted_values, color='skyblue')  # Create horizontal bars with sorted positions and values
    ax.set_xlim(0, 15)
    ax.set_yticks(y)
    ax.set_yticklabels([f'Bar {i+1}' for i in sorted_indices])
    ax.set_title(f'Horizontal Bar Chart for Year {years[i]}')
    # Add the value labels to the bars
    for bar, value in zip(bars, sorted_values):
        ax.text(bar.get_width() + 0.2, bar.get_y() + bar.get_height() / 2, str(value), va='center')

# Create a figure and axis
fig, ax = plt.subplots()

# Create the animation
ani = animation.FuncAnimation(fig, update_bar, frames=len(years), interval=1000, repeat=False)

# Show the animation
plt.show()
