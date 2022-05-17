# Install the BeautifulSoup module using CLI command: pip install beautifulsoup4 

from bs4 import BeautifulSoup
import csv
import requests

def get_addresses(input_file):
  # Get a list of addresses from the input file 'properties_sample.csv'
  with open(input_file, 'r') as f:
    read = csv.reader(f, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    address_list = [row for row in read]
  return address_list[1:]

def queries(addresses):
  # Create a list of links for a google search
  url_google = 'https://www.google.com/search?q='
  queries = []
  for address in addresses:
    address = str(','.join(address))
    address_base = address.replace(' ', '+')
    url_full = url_google + address_base + '+site:zillow.com'    
    queries.append(url_full)
  return queries

def get_soup(query):
  # Get a google search page for a single address
  resp = requests.get(query, timeout= 3.1)
  soup = BeautifulSoup(resp.text, "html.parser")
  return soup

def property_data(soup):
  # Parse property data from a google search page
  data = soup.find(class_=item_search_class)
  link = data.find('a').get('href').split('=')[1].split('&')[0]
  zpid = link.split('/')[-2].split('_')[0]
  text = data.text.split()
  #mls = text[text.index('MLS')+1][1:8]
  square, family, beds, baths = [text[text.index(q)-1] for q in ['Square', 'family', 'beds,', 'baths']]
  for_sale = ' '.join(text[text.index('is')+1:text.index('The')])[:-1]
  home_data = [link, zpid, for_sale, square, family, beds, baths]
  return home_data

def addr_data(address, data):
  # It merges the property data and the property address
  return address + data

def output_to_file(property_array):
  # It outputs the property data to the output file 'properties_data.csv'
  with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(property_array)

def main():
  # The 'main' function integrares an other functions
  addresses = get_addresses(input_file)
  querie = queries(addresses)
  # Headers of the table
  property_array = [['build&street',
                     'city',
                     'state',
                     'zip_code',
                     'link',
                     'zpid',
                     'for_sale',
                     'square feet',
                     'families',
                     'beds',
                     'baths'
                    ]] 
  for i, query in enumerate(querie):
    soup = get_soup(query)
    data = property_data(soup)
    data_full = addr_data(addresses[i], data)
    property_array.append(data_full)
  output_to_file(property_array) # Output to file
  # Print output array
  for row in property_array:
    print(row)

#config
input_file = 'properties_sample.csv'
output_file = 'properties_data.csv'
item_search_class = '<ENTER YOUR GOOGLE SEARCH CLASS>'

if __name__ == "__main__":
  main()

# Author: github.com/ogr42
