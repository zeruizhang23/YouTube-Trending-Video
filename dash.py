import dash
from dash import dcc, html, Input, Output
import plotly.express as px
from mywordcloud import generate_wordcloud  # Ensure this function is correctly defined in mywordcloud.py
from heatmap import create_heatmap_figure  # Adjust this function name based on your heatmap.py
from Top_5_videos import create_top_5_videos_figure  # Adjust this function name based on your Top_5_videos.py
from Top_10_Categories import create_top_10_categories_figure  # Adjust this function name based on your Top_10_Categories.py

app = dash.Dash(__name__)

app.layout = html.Div([
    html.Div([
        dcc.Graph(id='top-10-categories-chart', figure=create_top_10_categories_figure()),
        dcc.Graph(id='heatmap-chart', figure=create_heatmap_figure()),
    ], style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'top'}),

    html.Div([
        html.Img(id='word-cloud-image', style={'width': '100%', 'height': '400px'}),
        dcc.Graph(id='top-5-videos-chart', figure=create_top_5_videos_figure()),
    ], style={'width': '49%', 'display': 'inline-block', 'vertical-align': 'top'}),

    dcc.Dropdown(
        id='country-select',
        options=[
            {'label': 'United States', 'value': 'US'},
            {'label': 'Mexico', 'value': 'MX'},
            {'label': 'Canada', 'value': 'CA'}
        ],
        value='US'  # Default value
    ),
])

@app.callback(
    Output('word-cloud-image', 'src'),
    Input('country-select', 'value')
)
def update_word_cloud(selected_country):
    return generate_wordcloud(selected_country)

if __name__ == '__main__':
    app.run_server(debug=True)

