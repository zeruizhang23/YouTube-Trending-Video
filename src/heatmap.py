import plotly.express as px
import pandas as pd

def generate_heatmap(df, selected_metric ='view_count', metrics=['view_count', 'likes', 'comment_count']):
    df['publishedAt'] = pd.to_datetime(df['publishedAt'], errors='coerce')
    df['hour_of_day'] = df['publishedAt'].dt.hour
    df['day_of_week'] = df['publishedAt'].dt.dayofweek
    df['day_name'] = df['publishedAt'].dt.day_name()

    # Aggregate data for heatmap
    def aggregate_data(metrics):
        threshold = df[metrics].quantile(0.95)
        filtered_df = df[df[metrics] > threshold]
        heatmap_df = filtered_df.groupby(['day_of_week', 'hour_of_day', 'day_name'])[metrics].mean().reset_index()
        heatmap_df = heatmap_df.pivot('day_name', 'hour_of_day', metrics).fillna(0)
        return heatmap_df

    aggregated_data = aggregate_data(selected_metric)
    print(aggregated_data.shape)
    fig = px.imshow(
        aggregated_data,
        #labels=dict(x="Hour of Day", y="Day of Week", color=selected_metric.capitalize()),
        x=[str(i) for i in range(24)],
        y=['Mon.', 'Tues.', 'Wed.', 'Thurs.', 'Fri.', 'Sat.', 'Sun.'],
        color_continuous_scale='PuRd',
        aspect='auto'
    )
    
    fig.update_layout(
        xaxis_nticks=24,
        yaxis_nticks=7,
        margin=dict(t=20, l=20, b=20, r=20),
        hovermode='closest'
    )
    
    fig.update_coloraxes(colorscale='PuRd', colorbar_title_side='right')
    
    return fig
