# Job Listings Scraper and Analyzer

This project is a web scraping and data analysis application that collects job listings from job portals like Indeed, processes the data, and generates insights about job titles, companies, locations, and other trends. The project uses Python, Jupyter Notebooks, and various data science libraries for analysis and visualization.

## Features

- **Web Scraping**: Scrapes job listings from Indeed (or other job portals) based on specified search parameters.
- **Data Analysis**: Analyzes job listings data, including common job titles, companies, and locations.
- **Visualizations**: Generates bar charts, word clouds, and maps for a deeper understanding of job market trends.
- **CSV Export**: Saves scraped data to CSV files for further analysis or sharing.

## Project Structure








## Prerequisites

To run this project, you need Python 3.x and the following dependencies:

- **Python**: Version 3.8 or above
- **Pandas**
- **Matplotlib**
- **Seaborn**
- **WordCloud**
- **Geopandas**
- **Geopy**
- **Requests**
- **JupyterLab (Optional)**

You can install the dependencies using the provided `requirements.txt` or `environment.yml` file.

## Setup

### Using `requirements.txt`

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/job-listings-scraper-analyzer.git
    cd job-listings-scraper-analyzer
    ```

2. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

### Using `environment.yml` (Conda)

1. Create and activate the Conda environment:
    ```bash
    conda env create -f environment.yml
    conda activate job-listings-analyzer
    ```

2. Once the environment is activated, all dependencies will be installed.

## Usage

### Web Scraping

To scrape job listings from Indeed, run the `scraper.py` script:

```bash
python scraping/scraper.py
```

This will save the raw job listings data to data/job_listings_raw.csv.

### Data Analysis
For data analysis and insights, run the analyze.py script or open the analysis.ipynb Jupyter notebook:

```Running the script: python analysis/analyze.py
Running the Jupyter notebook: jupyter notebook analysis/analysis.ipynb
```

### Visualizations
To generate visualizations, run the respective Python scripts:

```Charts: python visualizations/charts.py

Location Map: python visualizations/location_map.py

Word Cloud: python visualizations/wordcloud.py
```

These scripts will generate visualizations like bar charts, maps, and word clouds to give insights into the job market trends.

### Contributing

Contributions are welcome! Feel free to open issues or submit pull requests




