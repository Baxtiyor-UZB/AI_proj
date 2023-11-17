import plotly.graph_objects as go
import plotly.io as pio

# Sample data for different years and countries
years = list(range(2000, 2021))  # 20 years from 2000 to 2020
countries = ['Uzbekistan', 'Russia', 'China', 'United States', 'United Kingdom']
publications_count = {
    'Uzbekistan': [30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130],
    'Russia': [40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140],
    'China': [50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150],
    'United States': [60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, 155, 160],
    'United Kingdom': [35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135]
}

# Create a figure
fig = go.Figure()

# Add a pie trace for the initial year with dynamic values for all countries
fig.add_trace(go.Pie(labels=countries, values=[publications_count[country][0] for country in countries], name=str(years[0]), hole=0.3))

# Update the layout
fig.update_layout(title='AI Publications in Different Countries Over the Years',
                  updatemenus=[dict(type="buttons",
                                    buttons=[dict(label="Play",
                                                  method="animate",
                                                  args=[None, {"frame": {"duration": 1000, "redraw": True},
                                                               "fromcurrent": True, "transition": {"duration": 300, "easing": "quadratic-in-out"}}])])])

# Create frames for the animation with dynamic values for all countries
frames = [go.Frame(data=[go.Pie(labels=countries, values=[publications_count[country][i] for country in countries], name=str(years[i]), hole=0.3)], name=str(year)) for i, year in enumerate(years)]

# Add frames to the figure
fig.frames = frames

# Save the animation as an HTML file
pio.write_html(fig, file='animated_dynamic_pie_chart_20_years.html', auto_open=False)

# Show the animation
fig.show()
