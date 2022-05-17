# Zillow data by google search
## This script gets zillow.com data ONLY by Google search.

The site zillow.com prohibits a data scraping. It shows the captcha, blocks ip-address etc.

But you can get this data!

This script gets data (addresses of property) in .csv format from the file 'properties_sample.csv'.

The script outputs data for each property address:
- address (build & street, city, state, zip_code);
- link to zillow.com;
- zpid from zillow.com;
- for sale or not for sale;
- square feet:
- number of families;
- number of beds;
- number of baths.

It outputs data in .csv formate to the file 'properties_data.csv' and to print.

Download this script to the directorie where is the input file 'properties_sample.csv'.

In row #84 'item_search_class = '<ENTER YOUR GOOGLE SEARCH CLASS>' ' paste html class wich Google Search gave to result search items.  
