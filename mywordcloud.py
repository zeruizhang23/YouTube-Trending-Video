import pandas as pd
from wordcloud import WordCloud
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from collections import Counter
import string
from io import BytesIO
import base64

# Ensure NLTK resources are downloaded
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet= True)

def clean_tokenize(text, stop_words):
    text = text.lower()
    text = text.translate(str.maketrans('', '', string.punctuation))
    words = text.split()
    words = [WordNetLemmatizer().lemmatize(word) for word in words if word not in stop_words] 
    words = [word for word in words if len(word) > 2 and not any(char.isdigit() for char in word)]
    return words

def generate_wordcloud(df, selected_country, width, height):
    additional_stopwords = set(['-', '|', 'official', 'trailer', '2023', '2024', 'video']) 
    stop_words = set(stopwords.words('english')) | additional_stopwords

    df_filtered = df[df['country'] == selected_country]
    df_filtered = df_filtered[~df_filtered['title'].str.contains('video', case=False)]
    text = " ".join(title for title in df_filtered['title'].dropna())
    words = clean_tokenize(text, stop_words)
    word_counts = Counter(words)
    
    wordcloud = WordCloud(width=width, height=height, background_color='white').generate_from_frequencies(word_counts)
    img = wordcloud.to_image()
    with BytesIO() as buffer:
        img.save(buffer, 'png')
        img_bytes = buffer.getvalue()
    img_base64 = base64.b64encode(img_bytes).decode()
    return f'data:image/png;base64,{img_base64}'
