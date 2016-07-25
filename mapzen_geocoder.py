#! /usr/bin/python3

from csv import DictReader, DictWriter
from time import sleep
import requests
infile = 'addresses.csv'
outfile = 'geocoded_' + infile
api_key = 'search-m7ga4cs'
base_url = 'https://search.mapzen.com/v1/search'
ca_min_lat = '32.53' 
ca_min_lon = '-124.48'
ca_max_lat = '42.01'
ca_max_lon = '-114.13'


def geocode(address_text):
    resp = requests.get(base_url,
    # Pass the API key, number of results and inputted address to the geocoder
    params = {'api_key': api_key, 'size': 1,
    'text': address_text, 
    # Search only within California
    'boundary.rect.min_lat': ca_min_lat, 
    'boundary.rect.min_lon': ca_min_lon, 
    'boundary.rect.max_lat': ca_max_lat, 
    'boundary.rect.max_lon': ca_max_lon})
    # Pass the JSON response to the variable data
    data = resp.json()
    # Pass the data in the features key to the variables features
    features = data['features']
    # Create a blank list and pass it to the variable pt
    pt = {}
    # Retrieve the latitude, longitude, confidence and returned address from the response
    pt['lat'] = (features[0]['geometry']['coordinates'][1])
    pt['lon'] = (features[0]['geometry']['coordinates'][0])
    pt['confidence'] = (features[0]['properties']['confidence'])
    pt['ret_address'] = (features[0]['properties']['label'])
    return pt


r = open(infile)
rcsv = DictReader(r)
w = open(outfile, 'w')
# Write the headers to the outfile
wcsv = DictWriter(w, fieldnames = rcsv.fieldnames + ['Latitude', 'Longitude', 'Returned Address', 'Confidence'])
wcsv.writeheader()
# Iterate through the infile line-by-line
for row in rcsv:
    # Pass the current line's street, city, state and ZIP columns to the variable input_addr
    input_addr = '%s, %s, %s, %s' % (row['Street'], row['City'], row['State'], row['ZIP'])
    # Geocode the current line and pass the result to the variable pt
    pt = geocode(input_addr)
    # Print the inputted address, the latitude, longitude, returned address and 
    # confidence to the terminal
    print(input_addr, pt['lat'], pt['lon'], pt['ret_address'], pt['confidence'])
    # Write the data for the new fields to the current line
    row['Latitude'] = pt['lat']
    row['Longitude'] = pt['lon']
    row['Returned Address'] = pt['ret_address']
    row['Confidence'] = pt['confidence']
    wcsv.writerow(row)
    # Wait one-tenth of a second between addresses
    sleep(0.1)

# Close the outfile and the infile
w.close()
r.close()
