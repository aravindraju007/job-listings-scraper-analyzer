import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
from shapely.geometry import Point

# Load the job listings data from the CSV file
file_path = 'data/job_listings_raw.csv'  # Path to your scraped CSV file
df = pd.read_csv(file_path)

# Function to geocode location to latitude and longitude using Geopy
def geocode_location(location):
    geolocator = Nominatim(user_agent="job_map")
    try:
        location_obj = geolocator.geocode(location)
        if location_obj:
            return location_obj.latitude, location_obj.longitude
        else:
            return None, None
    except Exception as e:
        print(f"Error geocoding {location}: {e}")
        return None, None

# Geocode all job locations and store latitude and longitude
df['Latitude'], df['Longitude'] = zip(*df['Location'].apply(geocode_location))

# Filter out rows with missing latitude/longitude
df = df.dropna(subset=['Latitude', 'Longitude'])

# Create a GeoDataFrame from the job locations
geometry = [Point(xy) for xy in zip(df['Longitude'], df['Latitude'])]
gdf = gpd.GeoDataFrame(df, geometry=geometry)

# Load a base world map for visualization
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))

# Plot the world map and job locations on top of it
fig, ax = plt.subplots(figsize=(15, 10))

# Plot the world map
world.plot(ax=ax, color='lightgray')

# Plot the job locations as red points
gdf.plot(ax=ax, marker='o', color='red', markersize=5)

# Set plot title and labels
plt.title("Job Locations", fontsize=16)
plt.xlabel("Longitude")
plt.ylabel("Latitude")

# Display the plot
plt.show()

