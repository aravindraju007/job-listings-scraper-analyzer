import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

# Base URL for the job search (adjust the query as needed)
BASE_URL = 'https://www.indeed.com/jobs?q=data+analyst&l=remote'

# Function to fetch job listings from a single page
def fetch_job_listings(page=1):
    # Construct the URL for the current page
    url = f'{BASE_URL}&start={page * 10}'  # Indeed paginates results with 'start=0', 'start=10', etc.
    
    # Send a GET request to the URL
    response = requests.get(url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve data from {url}")
        return []
    
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract job listings
    job_listings = []
    for job in soup.find_all('div', class_='jobsearch-SerpJobCard'):
        title = job.find('a', class_='jobtitle')
        company = job.find('span', class_='company')
        location = job.find('div', class_='location')
        summary = job.find('div', class_='summary')

        # Extract text if the elements exist
        job_listings.append({
            'Job Title': title.text.strip() if title else 'N/A',
            'Company': company.text.strip() if company else 'N/A',
            'Location': location.text.strip() if location else 'N/A',
            'Summary': summary.text.strip() if summary else 'N/A'
        })
    
    return job_listings

# Function to save job listings to CSV
def save_to_csv(job_listings, filename='data/job_listings_raw.csv'):
    # Create a DataFrame from the job listings
    df = pd.DataFrame(job_listings)
    
    # Save DataFrame to CSV
    df.to_csv(filename, index=False, mode='a', header=not pd.io.common.file_exists(filename))
    print(f"Saved {len(job_listings)} job listings to {filename}")

# Main function to scrape multiple pages and save the data
def main():
    all_job_listings = []
    total_pages = 5  # Number of pages to scrape, adjust as needed

    for page in range(total_pages):
        print(f"Scraping page {page + 1}...")
        
        # Fetch job listings from the current page
        job_listings = fetch_job_listings(page)
        
        # If there are no job listings, stop scraping
        if not job_listings:
            print("No more job listings found, stopping...")
            break
        
        # Add the job listings to the overall list
        all_job_listings.extend(job_listings)
        
        # Save data to CSV after each page
        save_to_csv(job_listings)
        
        # Sleep for a few seconds to avoid being blocked (adjust as needed)
        time.sleep(3)
    
    # After scraping all pages, save the final list of job listings to CSV
    if all_job_listings:
        print(f"Scraped {len(all_job_listings)} job listings in total.")
        save_to_csv(all_job_listings, filename='data/job_listings_raw.csv')
    else:
        print("No job listings scraped.")

if __name__ == '__main__':
    main()

