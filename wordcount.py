import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
from collections import Counter
import string

df = pd.read_csv('YouTube-Trending-Video.csv')

# Ensure the 'title' column is string
df['title'] = df['title'].astype(str)

# Concatenate all video titles
all_titles = ' '.join(df['title']).lower()

# Remove punctuation
all_titles = all_titles.translate(str.maketrans('', '', string.punctuation))

# Tokenization (split the string into words)
words = all_titles.split()

# Remove stopwords
words = [word for word in words if word not in stopwords.words('english')]

# Count the words
word_counts = Counter(words)

# Most common words
most_common_words = word_counts.most_common(25)

# Display the most common words
print("Most common words in video titles:")
for word, count in most_common_words:
    print(f"{word}: {count}")

# Create and display a word cloud
wordcloud = WordCloud(width = 800, height = 400, background_color ='white').generate(all_titles)

plt.figure(figsize = (10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

