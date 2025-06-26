import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Set up the plotting style
sns.set(style="whitegrid")

# Load the job listings data from the CSV file
file_path = 'data/job_listings_raw.csv'  # Path to your scraped CSV file
df = pd.read_csv(file_path)

# Display the first few rows of the dataframe
print("First few rows of the dataset:")
print(df.head())

# Check for missing values
print("\nMissing values in each column:")
print(df.isnull().sum())

# Data types and basic summary statistics
print("\nData Types and Basic Info:")
df_info = df.info()

print("\nSummary Statistics (for numerical columns if available):")
print(df.describe())

# Explore unique values in key columns
print("\nUnique values in key columns:")
print(f"Unique Job Titles: {df['Job Title'].nunique()}")
print(f"Unique Companies: {df['Company'].nunique()}")
print(f"Unique Locations: {df['Location'].nunique()}")

# Visualizations

# 1. Top 10 Job Titles
top_titles = df['Job Title'].value_counts().head(10)
plt.figure(figsize=(10, 6))
top_titles.plot(kind='barh', color='skyblue')
plt.title('Top 10 Most Common Job Titles')
plt.xlabel('Frequency')
plt.ylabel('Job Title')
plt.gca().invert_yaxis()
plt.show()

# 2. Top 10 Companies
top_companies = df['Company'].value_counts().head(10)
plt.figure(figsize=(10, 6))
top_companies.plot(kind='barh', color='lightcoral')
plt.title('Top 10 Companies with Most Job Postings')
plt.xlabel('Frequency')
plt.ylabel('Company')
plt.gca().invert_yaxis()
plt.show()

# 3. Top 10 Locations
top_locations = df['Location'].value_counts().head(10)
plt.figure(figsize=(10, 6))
top_locations.plot(kind='barh', color='lightgreen')
plt.title('Top 10 Job Locations')
plt.xlabel('Frequency')
plt.ylabel('Location')
plt.gca().invert_yaxis()
plt.show()

# 4. Word Cloud for Job Summaries
text = ' '.join(df['Summary'].dropna())
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

plt.figure(figsize=(10, 6))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.title('Word Cloud for Job Summaries')
plt.show()

# Save insights to CSV (optional)
top_titles_df = top_titles.reset_index()
top_titles_df.columns = ['Job Title', 'Frequency']
top_titles_df.to_csv('data/top_job_titles.csv', index=False)

print("\nTop job titles have been saved to 'top_job_titles.csv'.")

# Save any other insights or processed data you want to export to CSV here

