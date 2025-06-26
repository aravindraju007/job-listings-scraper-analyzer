import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
from config import BASE_URL, QUERY_PARAMS, SELECTORS, REQUEST_DELAY, OUTPUT_FILE

# Function to fetch job listings from a single page
def fetch_job_listings(page=1):
    # Construct the URL for the current page using the base URL and query parameters
    params = QUERY_PARAMS.copy()
    params['start'] = page * 10  # Pagination, Indeed uses 'start=0', 'start=10', etc.
    
    # Send a GET request to the URL with query parameters
    response = requests.get(BASE_URL, params=params, headers={'User-Agent': 'Mozilla/5.0'})
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve data from page {page}")
        return []

    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract job listings from the page
    job_listings = []
    for job in soup.find_all('div', class_=SELECTORS['job_card']):
        title = job.find('a', class_=SELECTORS['title'])
        company = job.find('span', class_=SELECTORS['company'])
        location = job.find('div', class_=SELECTORS['location'])
        summary = job.find('div', class_=SELECTORS['summary'])

        # Extract text if the elements exist
        job_listings.append({
            'Job Title': title.text.strip() if title else 'N/A',
            'Company': company.text.strip() if company else 'N/A',
            'Location': location.text.strip() if location else 'N/A',
            'Summary': summary.text.strip() if summary else 'N/A'
        })
    
    return job_listings

# Function to save job listings to a CSV file
def save_to_csv(job_listings, filename=OUTPUT_FILE):
    # Create a DataFrame from the job listings list
    df = pd.DataFrame(job_listings)
    
    # Check if the file already exists to append or create a new file
    df.to_csv(filename, mode='a', index=False, header=not pd.io.common.file_exists(filename))
    print(f"Saved {len(job_listings)} job listings to {filename}")

# Main function to scrape multiple pages and save the data to CSV
def main():
    all_job_listings = []
    total_pages = 5  # Set how many pages you want to scrape

    for page in range(total_pages):
        print(f"Scraping page {page + 1}...")
        
        # Fetch job listings from the current page
        job_listings = fetch_job_listings(page)
        
        # If there are no job listings, stop scraping
        if not job_listings:
            print(f"No more job listings found on page {page + 1}, stopping...")
            break
        
        # Add the job listings to the overall list
        all_job_listings.extend(job_listings)
        
        # Save the job listings to CSV after scraping the page
        save_to_csv(job_listings)
        
        # Sleep to prevent overwhelming the server
        time.sleep(REQUEST_DELAY)
    
    # After scraping all pages, save the final list to CSV
    if all_job_listings:
        print(f"Scraped {len(all_job_listings)} job listings in total.")
        save_to_csv(all_job_listings)
    else:
        print("No job listings scraped.")

if __name__ == '__main__':
    main()
