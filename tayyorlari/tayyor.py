import plotly.graph_objects as go

# Sample data for different organizations and years
organizations = ['Academy of Sciences Republic of Uzbekistan', 'National University of Uzbekistan', 'Samarkand State University',
                 'Tashkent State University of Economics', 'Tashkent University of Information Technology',
                 'Tashkent Institute of Irrigation and Agricultural Mechanization Engineers', 'Tashkent State Technical University named after Islam Karimov',
                 'Bukhara State University', 'Uzbek State University of World Languages', 'Tashkent Institute of Railway Transport Engineers']
years = list(range(2017, 2024))  # 7 years from 2017 to 2023
publications_count = {
    'Academy of Sciences Republic of Uzbekistan': [6, 11, 9, 16, 34, 26, 35],
    'National University of Uzbekistan': [7, 7, 22, 33, 61, 65, 70],
    'Samarkand State University': [2, 4, 9, 26, 32, 33, 37],
    'Tashkent State University of Economics': [3, 2, 7, 23, 45, 58, 0],
    'Tashkent University of Information Technology': [10, 9, 96, 106, 166, 98, 71],
    'Tashkent Institute of Irrigation and Agricultural Mechanization Engineers': [1, 15, 56, 64, 30, 78, 0],
    'Tashkent State Technical University named after Islam Karimov': [1, 2, 28, 74, 91, 41, 65],
    'Bukhara State University': [1, 0, 4, 24, 48, 24, 7],
    'Uzbek State University of World Languages': [2, 1, 6, 17, 34, 34, 17],
    'Tashkent Institute of Railway Transport Engineers': [0, 5, 10, 35, 27, 54, 0]
}

# Create a stacked bar chart
fig = go.Figure(data=[go.Bar(x=years, y=publications_count[organization], name=organization) for organization in organizations], layout=go.Layout(barmode='stack'))

# Update the layout
fig.update_layout(title='Number of Publications by Organization Over the Years', xaxis_title='Year', yaxis_title='Publications')

# Show the chart
fig.show()
