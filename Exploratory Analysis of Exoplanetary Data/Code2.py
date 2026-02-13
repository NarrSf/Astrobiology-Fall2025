import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (update the file path according to where the CSV file is stored on your computer)

file_path = '/Users/narges_sf/Downloads/exoplanet.eu_catalog_08-12-25_13_25_29.csv'
exoplanet_data = pd.read_csv(file_path)

filtered_data = exoplanet_data.dropna(subset=['orbital_period', 'semi_major_axis', 'star_teff'])

#Plot 1
plt.figure(figsize=(10, 6))
plt.scatter(filtered_data['semi_major_axis'], filtered_data['orbital_period'], alpha=0.7, color='purple')
plt.title('Orbital Period vs Semi-Major Axis')
plt.xlabel('Semi-Major Axis (AU)')
plt.ylabel('Orbital Period (Days)')
plt.grid(True)
plt.show()

# Plot 2
plt.figure(figsize=(10, 6))
plt.hist(filtered_data['star_teff'], bins=30, color='pink', edgecolor='black', alpha=0.7)
plt.title('Distribution of Star Temperature')
plt.xlabel('Star Temperature (K)')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
