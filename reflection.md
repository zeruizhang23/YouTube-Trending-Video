
# Dashboard Reflection

## Current Implementation

Our dashboard, designed to analyze and visualize YouTube trending video data, currently boasts a variety of interactive features. We've implemented four main visualizations: a heatmap, a word cloud, a list of top 5 videos, and a bar chart of top 10 categories. Users can filter results based on country selection, which dynamically updates all visual components to reflect region-specific data. 

The heatmap highlights the best times for video posting, while the word cloud presents common themes in video titles. The list of top 5 videos showcases the most viewed content, and the bar chart brings attention to the most popular categories.

## Known Issues

As of now, the dashboard is still in development, and some features may not function as intended. For instance:

- Country selection is not consistently applied across all visualizations due to variable handling of country codes.
- The ability to filter data based on time is absent. This means users cannot yet view trends within specific timeframes, which limits the depth of analysis the dashboard can offer

## Strengths

The dashboard excels in providing a quick, at-a-glance understanding of trending video characteristics. The visualizations are intuitive and offer interactive elements, such as hover details and dynamic filtering, enhancing the user experience.

## Limitations

The current limitations are mainly around data handling and performance:

- The dashboard is only as current as the data it's fed, and real-time updating is not yet implemented.
- Performance can lag when processing large datasets or when multiple users access the dashboard simultaneously.

## Future Improvements

Moving forward, we plan to:

- Optimize performance, especially for data processing and visualization rendering.
- Add more interactive elements, such as clickable videos that redirect to the actual YouTube page.
- We aim to enhance the dashboard's interactivity and analytical capabilities by introducing time-range filters and a draggable time-slider. This will empower users to uncover trends over selectable time periods, providing a more dynamic exploration of the data.

## Technical Challenges

- We encountered challenges with data preprocessing and ensuring that visualizations accurately reflect user selections. This was addressed by refining our Pandas data manipulation and enhancing our callback functions in Dash.
- One of the significant technical hurdles we encountered was dealing with Spanish language titles in the word cloud visualization. The inclusion of non-English words posed a challenge in filtering and accurately representing the data.

## Learning Outcomes

Through this project, we've gained valuable experience with Dash and Plotly for web-based data visualization, as well as a deeper understanding of user interaction patterns. It also improved our proficiency in data preprocessing with Pandas.

## Collaboration and Work Distribution

Our team adopted an Agile methodology, holding regular stand-ups to track progress and pivot as necessary. Tasks were distributed based on individual strengths, ensuring efficient progress while providing learning opportunities.

---
This reflection captures our dashboard's current state and future directions, acknowledging both its strengths and limitations. We are committed to its continuous improvement and look forward to addressing the noted issues and implementing the proposed enhancements.