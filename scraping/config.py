# Base URL for the job search
BASE_URL = 'https://www.indeed.com/jobs'

# Search query parameters
QUERY_PARAMS = {
    'q': 'data analyst',   # The job title you are searching for
    'l': 'remote',          # Job location (e.g., 'remote' or a specific city)
    'sort': 'date',         # Sort by most recent jobs
}

# Pagination configuration
PAGE_SIZE = 10  # Number of results per page (default on Indeed is 10)
MAX_PAGES = 10  # Maximum number of pages to scrape, adjust based on needs

# Output file path for saving job listings
OUTPUT_FILE = 'data/job_listings_raw.csv'

# Headers for HTTP requests (e.g., to mimic a real browser request and avoid being blocked)
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

# Delay between requests (to avoid overwhelming the server)
REQUEST_DELAY = 3  # Delay in seconds between requests to avoid rate limiting

# CSS Selectors for parsing job listings (may need to adjust if the site changes its structure)
SELECTORS = {
    'job_card': 'div.jobsearch-SerpJobCard',  # Selector for each individual job card
    'title': 'a.jobtitle',                    # Selector for job title
    'company': 'span.company',                # Selector for company name
    'location': 'div.location',               # Selector for job location
    'summary': 'div.summary',                 # Selector for job summary
}

# Pagination selectors (adjust if the pagination structure changes)
PAGINATION_SELECTORS = {
    'next_button': 'a[aria-label="Next"]',    # Selector for the "Next" button in pagination
}

# Max retries for requests in case of network issues
MAX_RETRIES = 3

# Timeout for each request (in seconds)
TIMEOUT = 10  # Timeout for requests to avoid hanging indefinitely

