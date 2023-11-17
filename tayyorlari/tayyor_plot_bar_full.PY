import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import seaborn as sns

# Read data from CSV
df = pd.read_csv('AI research by institution.csv')

# Group by organization and sum the total publications
total_publications = df.groupby(['Organization', 'Year'])['publications'].sum().unstack()

# Get unique colors for each organization
colors = sns.color_palette("husl", n_colors=len(total_publications.index))

# Create an animated horizontal bar chart with changing bar colors
fig, ax = plt.subplots(figsize=(11, 11))

# Map organization names to colors
color_mapping = {org: colors[i] for i, org in enumerate(total_publications.index)}

def update(frame):
    ax.clear()
    values = total_publications[frame].sort_values(ascending=False)
    color_values = [color_mapping[org] for org in values.index]
    bars = ax.barh(values.index, values, color=color_values)
    ax.set_title(f'Total Number of Publications by Organization in {frame}')
    ax.set_xlabel('Total Publications')
    ax.set_ylabel('Organization')

# Create an animation
animation = FuncAnimation(fig, update, frames=total_publications.columns, interval=3000, repeat=False)

# Show the animated plot
plt.show()