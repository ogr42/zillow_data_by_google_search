"""
Install the BeautifulSoup using CLI command:
pip install beautifulsoup4
""" 

from bs4 import BeautifulSoup
import csv
import requests

def get_addresses(input_file):
"""
Get the address list from the input file
"""
  with open(input_file, 'r') as f:
    read = csv.reader(f, delimiter=',', quotechar=',',
                        quoting=csv.QUOTE_MINIMAL)
    address_list = [row for row in read]
  return address_list[1:]

def queries(addresses):
"""
Create a links list for google search
"""
  url_google = 'https://www.google.com/search?q='
  queries = []
  for address in addresses:
    address = str(','.join(address))
    address_base = address.replace(' ', '+')
    url_full = url_google + address_base + '+site:zillow.com'    
    queries.append(url_full)
  return queries

def get_soup(query):
"""
Get a google search page for a single address
"""
  resp = requests.get(query, timeout= 3.1)
  soup = BeautifulSoup(resp.text, "html.parser")
  return soup

def property_data(soup):
"""
Parse property data from a google search page
"""
  data = soup.find('h3')
  head = data.text.split('|')
  mls = head[1].split('#')[1].strip() if 'MLS' in head[1] else ''
  address = head[0].strip()
  link = data.find_parent().get('href').split('=')[1][:-3]
  zpid = link.split('/')[-2].split('_')[0]
  text = data.find_parent().find_parent().find_parent().find_all()[5].text.split()
  square, family, beds, baths = [text[text.index(q)-1] for q in ['Square', 'family', 'beds,', 'baths']]
  for_sale = ' '.join(text[text.index('is')+1:text.index('The')])[:-1]
  home_data = [link, zpid, mls, square, family, beds, baths, for_sale]
  return home_data

def addr_data(address, data):
"""
Merge property data and property address
"""
  return address + data

def output_to_file(property_array):
"""
Output property data to the output file
"""
  with open(output_file, 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(property_array)

def main():
"""
Integrate all functions
"""
  addresses = get_addresses(input_file)
  query = queries(addresses)
  # Headers of the output table
  property_array = [['build&street',
                     'city',
                     'state',
                     'zip_code',
                     'link',
                     'zpid',
                     'mls', 
                     'square feet',
                     'families',
                     'beds',
                     'baths',
                     'for_sale'
                    ]] 
  for i, q in enumerate(query):
    soup = get_soup(q)
    data = property_data(soup)
    data_full = addr_data(addresses[i], data)
    property_array.append(data_full)
  output_to_file(property_array) # Output to file
  # Print the output array
  for row in property_array:
    print(row)

""" 
Configuration
"""
input_file = 'properties_sample.csv'
output_file = 'properties_data.csv'


if __name__ == "__main__":
  main()

# © Alex Romanoff, github.com/ogr42
# My Upwork: https://www.upwork.com/freelancers/~016af1ee0d7ed4ac4a
