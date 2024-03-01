import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc
from dash.dependencies import Input, Output

# Load the dataset
df = pd.read_csv('YouTube-Trending-Video.csv')

# Filter out rows where 'country' is null or missing
df = df[df['country'].notna()]

# Create the Dash app
app = Dash(__name__)

# Add an 'All' option to the list of countries
countries = df['country'].unique()
dropdown_options = [{'label': 'All', 'value': 'All'}] + [{'label': country, 'value': country} for country in countries]

# Define the app layout
app.layout = html.Div([
    html.H1('Top 10 Most Popular YouTube Video Categories'),
    dcc.Dropdown(
        id='country-dropdown',
        options=dropdown_options,
        value='All',  # Set 'All' as the default value
        clearable=False,
    ),
    dcc.Graph(id='category-popularity-plot')
])

# Callback to update the graph based on dropdown selection
@app.callback(
    Output('category-popularity-plot', 'figure'),
    [Input('country-dropdown', 'value')]
)
def update_figure(selected_country):
    # If 'All' is selected, use the full dataset; otherwise, filter by the selected country
    if selected_country == 'All':
        filtered_df = df
    else:
        filtered_df = df[df['country'] == selected_country]

    category_counts = filtered_df['categoryName'].value_counts().nlargest(10)

    fig = px.bar(category_counts, orientation='h', color=category_counts.index,
                 labels={'value': 'Number of Videos', 'index': 'Category'},
                 title=f'Top 10 Most Popular Categories in {selected_country}')

    fig.update_layout(yaxis={'categoryorder': 'total ascending'})
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
