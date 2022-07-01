# Zillow data parser by google search
## This script gets zillow.com data ONLY by Google search.

The site zillow.com prohibits data scraping. It shows the captcha, blocks IP-address, etc.

But you can get this data!

This script gets data (addresses of property) in .csv format from the input file 'properties_sample.csv'.

The script outputs data for each property address:
- address (build & street, city, state, zip_code);
- link to zillow.com;
- zpid from zillow.com;
- for sale or not for sale;
- square:
- a number of families;
- a number of beds;
- a number of baths.

It outputs data in .csv format to the file 'properties_data.csv' and to print.

Symply copy this script to the directory where is the input file 'properties_sample.csv' and run it.

In row #84 'item_search_class = '<ENTER YOUR GOOGLE SEARCH CLASS>' ' paste html class which Google Search gave to result from search items.  
