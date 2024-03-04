import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import pandas as pd
import dash_bootstrap_components as dbc
from heatmap import generate_heatmap
from mywordcloud import generate_wordcloud
from Top_5_videos import generate_top5_videos
from Top_10_Categories import generate_top10_categories

df = pd.read_csv("Youtube-Trending-Video.csv")

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(html.H1('YouTube Trending Videos Dashboard'), width=12)
    ]),
    dbc.Row([
        dbc.Col([
            html.Div([
                dcc.Dropdown(
                    id='country-dropdown',
                    options=[{'label': country, 'value': country} for country in df['country'].dropna().unique()],
                    value='Canada'
                ),
                html.Img(id='wordcloud-image')
            ]),
            dcc.Dropdown(
                id='heatmap-metric-selector',
                options=[
                    {'label': 'View Count', 'value': 'view_count'},
                    {'label': 'Likes', 'value': 'likes'},
                    {'label': 'Comment Count', 'value': 'comment_count'}
                ],
                value='view_count'
             ),
            dcc.Graph(id='heatmap-graph')
        ], md=6),
        dbc.Col([
            dcc.Dropdown(
                id='country-selector',
                options = [{'label': country, 'value': country} for country in df['country'].dropna().unique()],
                value='US',
                style={'width': '100%', 'margin-bottom': '20px'}
            ),
            html.Div(id='top-5-videos-content'),
            html.H1('Top 10 Most Popular YouTube Video Categories'),
            dcc.Dropdown(
                id='country-choose',
                options=[{'label': 'All', 'value': 'All'}]+[{'label': country, 'value': country} for country in df['country'].dropna().unique()],
                value='All',
                clearable=False,
            ),
            dcc.Graph(id='top-10-categories-graph')
        ], md=6)
    ])
], fluid=True)


@app.callback(
    Output('wordcloud-image', 'src'),
    [Input('country-dropdown', 'value')]
)
def update_image(selected_country):
    return generate_wordcloud(df, selected_country, width=700, height=300)

@app.callback(
    Output('heatmap-graph', 'figure'),
    [Input('heatmap-metric-selector', 'value')]
)
def update_heatmap(selected_metric):
    return generate_heatmap(df, selected_metric)

@app.callback(
    Output('top-5-videos-content', 'children'),
    [Input('country-selector', 'value')]
)
def update_top5_videos(selected_country):
    return generate_top5_videos(df,selected_country)

@app.callback(
    Output('top-10-categories-graph', 'figure'),
    [Input('country-choose', 'value')]
)
def update_top10_categories(selected_country):
    return generate_top10_categories(df,selected_country)

if __name__ == '__main__':
    app.run_server(debug=True)