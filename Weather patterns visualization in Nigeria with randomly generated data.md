```python
pip install dash plotly pandas
```

    Requirement already satisfied: dash in c:\users\testing\anaconda3\lib\site-packages (2.11.1)
    Requirement already satisfied: plotly in c:\users\testing\anaconda3\lib\site-packages (5.9.0)
    Requirement already satisfied: pandas in c:\users\testing\anaconda3\lib\site-packages (1.4.4)
    Requirement already satisfied: dash-core-components==2.0.0 in c:\users\testing\anaconda3\lib\site-packages (from dash) (2.0.0)
    Requirement already satisfied: nest-asyncio in c:\users\testing\anaconda3\lib\site-packages (from dash) (1.5.5)
    Requirement already satisfied: Flask<2.3.0,>=1.0.4 in c:\users\testing\anaconda3\lib\site-packages (from dash) (1.1.2)
    Requirement already satisfied: requests in c:\users\testing\anaconda3\lib\site-packages (from dash) (2.28.1)
    Requirement already satisfied: dash-html-components==2.0.0 in c:\users\testing\anaconda3\lib\site-packages (from dash) (2.0.0)
    Requirement already satisfied: ansi2html in c:\users\testing\anaconda3\lib\site-packages (from dash) (1.8.0)
    Requirement already satisfied: dash-table==5.0.0 in c:\users\testing\anaconda3\lib\site-packages (from dash) (5.0.0)
    Requirement already satisfied: typing-extensions>=4.1.1 in c:\users\testing\anaconda3\lib\site-packages (from dash) (4.3.0)
    Requirement already satisfied: Werkzeug<2.3.0 in c:\users\testing\anaconda3\lib\site-packages (from dash) (2.0.3)
    Requirement already satisfied: retrying in c:\users\testing\anaconda3\lib\site-packages (from dash) (1.3.4)
    Requirement already satisfied: tenacity>=6.2.0 in c:\users\testing\anaconda3\lib\site-packages (from plotly) (8.0.1)
    Requirement already satisfied: numpy>=1.18.5 in c:\users\testing\anaconda3\lib\site-packages (from pandas) (1.21.5)
    Requirement already satisfied: python-dateutil>=2.8.1 in c:\users\testing\anaconda3\lib\site-packages (from pandas) (2.8.2)
    Requirement already satisfied: pytz>=2020.1 in c:\users\testing\anaconda3\lib\site-packages (from pandas) (2022.1)
    Requirement already satisfied: Jinja2>=2.10.1 in c:\users\testing\anaconda3\lib\site-packages (from Flask<2.3.0,>=1.0.4->dash) (2.11.3)
    Requirement already satisfied: click>=5.1 in c:\users\testing\anaconda3\lib\site-packages (from Flask<2.3.0,>=1.0.4->dash) (8.0.4)
    Requirement already satisfied: itsdangerous>=0.24 in c:\users\testing\anaconda3\lib\site-packages (from Flask<2.3.0,>=1.0.4->dash) (2.0.1)
    Requirement already satisfied: six>=1.5 in c:\users\testing\anaconda3\lib\site-packages (from python-dateutil>=2.8.1->pandas) (1.16.0)
    Requirement already satisfied: certifi>=2017.4.17 in c:\users\testing\anaconda3\lib\site-packages (from requests->dash) (2022.9.14)
    Requirement already satisfied: urllib3<1.27,>=1.21.1 in c:\users\testing\anaconda3\lib\site-packages (from requests->dash) (1.26.11)
    Requirement already satisfied: idna<4,>=2.5 in c:\users\testing\anaconda3\lib\site-packages (from requests->dash) (3.3)
    Requirement already satisfied: charset-normalizer<3,>=2 in c:\users\testing\anaconda3\lib\site-packages (from requests->dash) (2.0.4)
    Requirement already satisfied: colorama in c:\users\testing\anaconda3\lib\site-packages (from click>=5.1->Flask<2.3.0,>=1.0.4->dash) (0.4.5)
    Requirement already satisfied: MarkupSafe>=0.23 in c:\users\testing\anaconda3\lib\site-packages (from Jinja2>=2.10.1->Flask<2.3.0,>=1.0.4->dash) (2.0.1)
    Note: you may need to restart the kernel to use updated packages.
    


```python
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

```



<iframe
    width="100%"
    height="650"
    src="http://127.0.0.1:8050/"
    frameborder="0"
    allowfullscreen

></iframe>


