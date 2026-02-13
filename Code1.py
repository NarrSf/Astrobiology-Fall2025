import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset (update the file path according to where the CSV file is stored on your computer)

file_path = '/Users/narges_sf/Downloads/exoplanet.eu_catalog_08-12-25_13_25_29.csv'
exoplanet_data = pd.read_csv(file_path)

filtered_data = exoplanet_data.dropna(subset=['mass', 'radius'])

def categorize_planet(row):
    if row['mass'] < 0.5:
        return 'Small'
    elif row['mass'] < 2:
        return 'Medium'
    else:
        return 'Large'

filtered_data['mass_category'] = filtered_data.apply(categorize_planet, axis=1)

plt.figure(figsize=(10, 6))

plt.scatter(filtered_data['mass'], filtered_data['radius'], 
            c=filtered_data['mass_category'].map({'Small': 'blue', 'Medium': 'orange', 'Large': 'purple'}), 
            alpha=0.7, marker='x')  

plt.title('Planet Mass vs Radius')
plt.xlabel('Mass (M_Jupiter)')
plt.ylabel('Radius (R_Jupiter)')
plt.legend(['Small', 'Medium', 'Large'])
plt.grid(True)
plt.show()
