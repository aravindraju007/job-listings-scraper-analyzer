import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set up the plotting style
sns.set(style="whitegrid")

# Load the job listings data from the CSV file
file_path = 'data/job_listings_raw.csv'  # Path to your scraped CSV file
df = pd.read_csv(file_path)

# 1. Plot Top 10 Most Common Job Titles
def plot_top_job_titles():
    top_titles = df['Job Title'].value_counts().head(10)
    plt.figure(figsize=(10, 6))
    top_titles.plot(kind='barh', color='skyblue')
    plt.title('Top 10 Most Common Job Titles')
    plt.xlabel('Frequency')
    plt.ylabel('Job Title')
    plt.gca().invert_yaxis()  # Invert y-axis for better visualization
    plt.show()

# 2. Plot Top 10 Companies with the Most Job Postings
def plot_top_companies():
    top_companies = df['Company'].value_counts().head(10)
    plt.figure(figsize=(10, 6))
    top_companies.plot(kind='barh', color='lightcoral')
    plt.title('Top 10 Companies with Most Job Postings')
    plt.xlabel('Frequency')
    plt.ylabel('Company')
    plt.gca().invert_yaxis()  # Invert y-axis for better visualization
    plt.show()

# 3. Plot Top 10 Job Locations
def plot_top_locations():
    top_locations = df['Location'].value_counts().head(10)
    plt.figure(figsize=(10, 6))
    top_locations.plot(kind='barh', color='lightgreen')
    plt.title('Top 10 Job Locations')
    plt.xlabel('Frequency')
    plt.ylabel('Location')
    plt.gca().invert_yaxis()  # Invert y-axis for better visualization
    plt.show()

# 4. Plot Job Title Distribution (Count of Each Job Title)
def plot_job_title_distribution():
    plt.figure(figsize=(12, 8))
    df['Job Title'].value_counts().plot(kind='bar', color='lightblue')
    plt.title('Job Title Distribution')
    plt.xlabel('Job Title')
    plt.ylabel('Number of Job Listings')
    plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
    plt.show()

# 5. Plot the Distribution of Locations for Job Listings
def plot_location_distribution():
    plt.figure(figsize=(12, 8))
    df['Location'].value_counts().plot(kind='bar', color='lightpink')
    plt.title('Location Distribution for Job Listings')
    plt.xlabel('Location')
    plt.ylabel('Number of Job Listings')
    plt.xticks(rotation=90)  # Rotate x-axis labels for better readability
    plt.show()

# 6. Plot Word Frequency (Top Words in Job Summaries)
def plot_word_frequency():
    from wordcloud import WordCloud
    
    # Combine all job summaries into one large text
    text = ' '.join(df['Summary'].dropna())
    
    # Create a WordCloud from the job summaries
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    # Plot the word cloud
    plt.figure(figsize=(10, 6))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.title('Word Cloud for Job Summaries')
    plt.show()

# Call functions to plot the charts
plot_top_job_titles()
plot_top_companies()
plot_top_locations()
plot_job_title_distribution()
plot_location_distribution()
plot_word_frequency()

