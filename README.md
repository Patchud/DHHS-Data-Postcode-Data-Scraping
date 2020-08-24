# DHHS-Data-Postcode-Data-Scraping
Scrapes the data from the DHHS website using JSON API calls.

This program returns an aggregate of the postcode data printed to screen as a JSON string. The output of this program can then be redirected, to a file so that data analytics can be performed.

The JSON will follow this format

{\
  id: {\
        'postcode': 3975,\
        '_new': 1,\
        'activedisp': 'Five or fewer active cases',\
        'cases': 37,\
        'ratedisp': 16,\
        'population': 15246\
  }\
}\
