#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
df = pd.read_csv('YouTube-Trending-Video.csv')


# In[8]:


import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Dropdown for country selection
country_dropdown = dcc.Dropdown(
    id='country-dropdown',
    options=[
        {'label': 'Canada', 'value': 'Canada'},
        {'label': 'USA', 'value': 'US'},
        {'label': 'Mexico', 'value': 'Mexico'}
    ],
    value='US',  # Default value
    style={'width': '50%', 'margin-bottom': '20px'}
)

# Placeholder for the videos content, to be filled in by the callback
videos_content = html.Div(id='videos-content')

app.layout = html.Div([
    country_dropdown,
    videos_content
])

@app.callback(
    Output('videos-content', 'children'),
    [Input('country-dropdown', 'value')]
)
def update_videos(selected_country):
    filtered_df = df[df['country'] == selected_country]
    top_videos = filtered_df.sort_values(by='view_count', ascending=False).drop_duplicates(subset=['video_id'])
    top_videos = top_videos.iloc[:, [1,8,9,10,11,12]]
    top_5videos = top_videos.head()
    
    rows = []
    for _, row in top_5videos.iterrows():
        video_info = dbc.Col([
            html.H5(row['title'], className='mt-0'),
            html.P(f"Views: {row['view_count']}   Comments: {row['comment_count']}", style={'margin-bottom': '2px'}),
            html.P(f"Likes: {row['likes']}   Dislikes: {row['dislikes']}", style={'margin-bottom': '2px'})
        ], width=8)

        thumbnail = dbc.Col([
            html.Img(src=row['thumbnail_link'], style={'width': '100px', 'height': 'auto'})
        ], width=2)

        video_row = dbc.Row([thumbnail, video_info], className='mb-3')
        rows.append(video_row)
    
    return rows

if __name__ == '__main__':
    app.run_server(debug=True)


# In[ ]:




