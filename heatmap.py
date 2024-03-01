import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import pandas as pd

df = pd.read_csv("YouTube-Trending-Video.csv")

# Assuming df is your DataFrame loaded with the YouTube data
df['publishedAt'] = pd.to_datetime(df['publishedAt'])
df['hour_of_day'] = df['publishedAt'].dt.hour
df['day_of_week'] = df['publishedAt'].dt.dayofweek
df['day_name'] = df['publishedAt'].dt.day_name()

# # Normalize the engagement metrics
metrics = ['view_count', 'likes', 'comment_count']
# df[metrics] = df[metrics].apply(lambda x: x / x.max())

# Aggregate data for heatmap
def aggregate_data(metric):
    threshold = df[metric].quantile(0.95)
    filtered_df = df[df[metric] > threshold]
    heatmap_df = filtered_df.groupby(['day_of_week', 'hour_of_day', 'day_name'])[metric].mean().reset_index()
    heatmap_df = heatmap_df.pivot('day_name', 'hour_of_day', metric).fillna(0)
    return heatmap_df

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the dashboard
app.layout = html.Div([
    html.H1('Optimal Posting Times for Maximum Engagement'),
    dcc.Dropdown(
        id='metric-selector',
        options=[{'label': metric.capitalize(), 'value': metric} for metric in metrics],
        value='view_count'  # Default value
    ),
    dcc.Graph(id='heatmap-graph')
])

# Callback to update the heatmap based on selected metric
@app.callback(
    Output('heatmap-graph', 'figure'),
    [Input('metric-selector', 'value')]
)
def update_heatmap(selected_metric):
    aggregated_data = aggregate_data(selected_metric)
    fig = px.imshow(
        aggregated_data,
        labels=dict(x="Hour of Day", y="Day of Week", color=selected_metric.capitalize()),
        x=[str(i) for i in range(24)],  # Explicitly set the x-axis labels
        y=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
        color_continuous_scale='PuRd',
        aspect='auto'
    )
    
    # Improve the layout and enable more useful zoom
    fig.update_layout(
        xaxis_nticks=24,  # Show all hours
        yaxis_nticks=7,  # Show all days
        margin=dict(t=50, l=50, b=50, r=50),  # Adjust margins to fit
        hovermode='closest'  # Improves hover interaction
    )
    
    # Enable the color axis to be dynamic based on the data, improving contrast
    fig.update_coloraxes(colorscale='PuRd', colorbar_title_side='right')
    
    return fig

# Run the Dash app
if __name__ == '__main__':
    app.run_server(debug=True)
