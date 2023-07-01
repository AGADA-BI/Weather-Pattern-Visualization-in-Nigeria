#!/usr/bin/env python
# coding: utf-8

# In[21]:


pip install dash plotly pandas


# In[26]:


get_ipython().system('pip install dash dash-core-components dash-html-components pandas')


# In[28]:


import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
from datetime import datetime, timedelta
import random

# Generate random weather data for visualization
start_date = datetime(2023, 1, 1)
end_date = datetime(2023, 3, 31)
date_range = pd.date_range(start_date, end_date)

# Randomly generate temperature and precipitation values
temperature = [random.uniform(0, 30) for _ in range(len(date_range))]
precipitation = [random.uniform(0, 10) for _ in range(len(date_range))]

# Create a DataFrame using the generated data
df = pd.DataFrame({'date': date_range, 'temperature': temperature, 'precipitation': precipitation})

# Start the dash app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div(
    children=[
        html.H1("Weather Patterns in the Nigeria"),
        dcc.Graph(
            id="weather-graph",
            figure={
                'data': [
                    {'x': df['date'], 'y': df['temperature'], 'type': 'line', 'name': 'Temperature', 'line': {'color': 'black'}},
                    {'x': df['date'], 'y': df['precipitation'], 'type': 'bar', 'name': 'Precipitation', 'marker': {'color': 'orange'}},
                ],
                'layout': {
                    'title': 'Weather Patterns',
                    'xaxis': {'title': 'Date'},
                    'yaxis': {'title': 'Temperature / Precipitation'},
                }
            }
        )
    ]
)


# Run the app
app.run_server(mode='inline')


# In[ ]:




