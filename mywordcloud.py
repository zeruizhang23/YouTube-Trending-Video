import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
from collections import Counter
import string
import dash
import dash_html_components as html


app = dash.Dash()
app.layout = html.Div('worldcloud')
app.run_server()

# Ensure NLTK resources are downloaded
nltk.download('stopwords')
nltk.download('wordnet')

# Load the dataset from your local file system
# Make sure to replace 'YouTube-Trending-Video.csv' with your actual file path
df = pd.read_csv('YouTube-Trending-Video.csv')

df_usa = df[df['country'] == 'MX']
# Combine all titles into a single string
text = " ".join(title for title in df['title'].dropna())

# Define additional stopwords
additional_stopwords = set(['-', '|', 'official', 'trailer', '2023', '2024'])  # Add more words here

# Combine NLTK stopwords with additional stopwords
stop_words = set(stopwords.words('english')) | additional_stopwords

# Initialize lemmatizer
lemmatizer = WordNetLemmatizer()

# Function to clean, tokenize, and lemmatize text
def clean_tokenize(text):
    # Convert text to lowercase
    text = text.lower()
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Split text into words
    words = text.split()
    # Lemmatize words (you may want to use a stemmer instead)
    words = [lemmatizer.lemmatize(word) for word in words]
    # Remove stopwords and short words
    words = [word for word in words if word not in stop_words and len(word) > 2]
    # Remove words with numbers
    words = [word for word in words if not any(char.isdigit() for char in word)]
    return words

# Tokenize the text
words = clean_tokenize(text)

# Count the words
word_counts = Counter(words)

# Generate word cloud
wordcloud = WordCloud(width=800, height=400, background_color='white').generate_from_frequencies(word_counts)

# Display the generated word cloud
plt.figure(figsize=(15, 7))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()




