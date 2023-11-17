import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

# Read data from CSV
df = pd.read_csv('publications_data.csv')

# Group by organization and sum the total publications
total_publications = df.groupby(['Organization', 'Year'])['Publications'].sum().unstack()

# Get unique colors for each organization
colors = px.colors.qualitative.Set1

# Create an animated horizontal bar chart with changing bar colors using Plotly Express
fig = px.bar()

# Map organization names to colors
color_mapping = {org: colors[i % len(colors)] for i, org in enumerate(total_publications.index)}

frames = [go.Frame(
    data=[
        go.Bar(
            x=total_publications[year].sort_values(ascending=False),
            y=total_publications[year].sort_values(ascending=False).index,
            orientation='h',
            marker=dict(color=[color_mapping[org] for org in total_publications[year].sort_values(ascending=False).index]),
            name=f'Total Publications in {year}'
        )
    ],
    name=f'{year}'
) for year in total_publications.columns]

fig.frames = frames

fig.update_layout(
    barmode='stack',
    title='Number of Publications by Organization Over the Years',
    xaxis_title='Total Publications',
    yaxis_title='Organization',
    updatemenus=[
        {
            'type': 'buttons',
            'showactive': False,
            'buttons': [
                {
                    'label': 'Play',
                    'method': 'animate',
                    'args': [None, {
                        'frame': {'duration': 1000, 'redraw': True},
                        'fromcurrent': True,
                        'mode': 'immediate',
                    }]
                },
                {
                    'label': 'Pause',
                    'method': 'animate',
                    'args': [[None], {
                        'frame': {'duration': 0, 'redraw': True},
                        'mode': 'immediate',
                        'transition': {'duration': 0}
                    }]
                }
            ],
        }
    ],
    sliders=[{
        'yanchor': 'top',
        'xanchor': 'left',
        'currentvalue': {
            'font': {'size': 16},
            'prefix': 'Year:',
            'visible': True,
            'xanchor': 'right'
        },
        'transition': {'duration': 300, 'easing': 'cubic-in-out'},
        'steps': [{
            'args': [[f'{year}']],
            'label': f'{year}',
            'method': 'animate',
        } for year in total_publications.columns]
    }]
)

fig.show()
