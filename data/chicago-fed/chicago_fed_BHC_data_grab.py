"""
Grabs the entire Federal Reserve Bank of Chicago Commercial Bank and Bank 
Holding Company database.

"""
__author__ = 'David R. Pugh'
__license__ = 'BSD'

import requests

base_url = "https://www.chicagofed.org/applications/bhc_data/bhcdata_create_output.cfm?"

for year in range(1987, 2015):
    for quarter in range(1, 5):
        
        # ...make the connection and grab the zipped files...
        tmp_query = {'DYR':str(year),'DQTR':str(quarter)}
        tmp_buffer = requests.get(url=base_url, params=tmp_query)
        
        # ...save them to disk...
        with open(('BHCD_{yr}Q{qtr}.zip').format(yr=year, qtr=quarter), 'wb') as tmp_zip_file:
            tmp_zip_file.write(tmp_buffer.content)    
    
    print('Done with files for ' + str(year) + '!')