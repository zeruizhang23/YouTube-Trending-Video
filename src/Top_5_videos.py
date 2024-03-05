import dash_bootstrap_components as dbc
from dash import html

def generate_top5_videos(df, selected_country='US'):
    filtered_df = df[df['country'] == selected_country]
    top_videos = filtered_df.sort_values(by='view_count', ascending=False).drop_duplicates(subset=['video_id'])
    top_videos = top_videos.iloc[:, [1,8,9,10,11,12]]
    top_5videos = top_videos.head(5)
    
    rows = []
    for _, row in top_5videos.iterrows():
        video_info = dbc.Col([
            html.H6(row['title'], className='mt-2', style={'white-space': 'normal'}),
            html.P(f"Views: {row['view_count']}", style={'margin-bottom': '2px', 'white-space': 'normal'}),
            html.P(f"Comments: {row['comment_count']}", style={'margin-bottom': '2px', 'white-space': 'normal'}),
            html.P(f"Likes: {row['likes']}", style={'margin-bottom': '2px', 'white-space': 'normal'})
        ], width=6, style={'padding-right': '10px'})

        thumbnail = dbc.Col([
            html.Img(src=row['thumbnail_link'], style={'width': '180px', 'height': 'auto','display': 'block', 'margin-left': 'auto', 'margin-right': 'auto'})
        ], width=6)

        video_row = dbc.Row([thumbnail, video_info], className='mb-3')
        rows.append(video_row)
    
    return rows
