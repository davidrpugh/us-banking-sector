"""
Grabs the entire Federal Reserve Bank of Chicago Commercial Bank and Bank 
Holding Company database.

"""
import requests

base_url = 'https://www.chicagofed.org/applications/bhc_data/bhcdata_create_output.cfm?'

for year in range(1986, 2015):
    
    tmp_query = {'DYR':year, 
                 'DQTR':[1-4]}
        
    # ...make the connection and grab the zipped files...
    tmp_buffer = requests.get(url=base_url, params=tmp_query)

    # ...save them to disk...
    with open('BHCD_' + str(year) + '.zip', 'wb') as tmp_zip_file:
        tmp_zip_file.write(tmp_buffer.content)    
    
    print('Done with files for ' + str(year) + '!')