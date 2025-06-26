import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Load the job listings data from the CSV file
file_path = 'data/job_listings_raw.csv'  # Path to your scraped CSV file
df = pd.read_csv(file_path)

# Combine all job summaries into one large text
text = ' '.join(df['Summary'].dropna())

# Generate the word cloud from the combined text
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

# Plot the word cloud
plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud for Job Summaries', fontsize=16)
plt.show()

