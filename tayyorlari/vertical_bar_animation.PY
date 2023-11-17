import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
# Sample data for different organizations and years
organizations = ['Org1', 'Org2', 'Org3', 'Org4', 'Org5']
years = list(range(2017, 2024))  # 7 years from 2017 to 2023
publications_count = {
    'Org1': [6, 11, 9, 16, 34, 26, 35],
    'Org2': [7, 7, 22, 33, 61, 65, 70],
    'Org3': [2, 4, 9, 26, 32, 33, 37],
    'Org4': [3, 2, 7, 23, 45, 58, 0],
    'Org5': [10, 9, 96, 106, 166, 98, 71],
}
# Find the maximum length of data among organizations
max_length = max(len(publications_count[org]) for org in organizations)
# Pad shorter sequences with zeros
padded_data = {org: np.pad(publications_count[org], (0, max_length - len(publications_count[org])), 'constant') for org in organizations}
# Function to update the plot for each frame
def update(frame):
    plt.cla()  # Clear the previous plot
    for i, org in enumerate(organizations):
        plt.bar(i, padded_data[org][frame], label=org, color='skyblue')
    plt.xlabel('Organizations')
    plt.ylabel('Publications')
    plt.title(f'Number of Publications by Organization in {years[frame]}')
    plt.xticks(range(len(organizations)), organizations)
    plt.legend()
# Create the initial plot
fig, ax = plt.subplots()
update(0)  # Display the first frame
# Create an animation
animation = FuncAnimation(fig, update, frames=len(years), interval=1000, repeat=False)
# Show the animated horizontal bar chart
plt.show()
