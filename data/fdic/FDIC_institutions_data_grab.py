"""
Grabs the entire Federal Deposit Insurance Corporation (FDIC) institutions data
set which catalogues the history of mergers and acquisitions for all FDIC
regulated instutitions and turns it into a Pandas DataFrame and picles the
object for future use.

"""
import zipfile

import pandas as pd
import requests

# download the data
base_url = 'http://www2.fdic.gov/IDASP/'
filename = 'Institutions2.zip'
tmp_buffer = requests.get(base_url + filename)

with open(filename, 'wb') as tmp_zip_file:
    tmp_zip_file.write(tmp_buffer.content)

# convert to pandas DataFrame
tmp_buffer = zipfile.ZipFile(filename)
tmp_file = tmp_buffer.namelist()[1]

used_cols = ['CERT', 'CHANGEC1']
dtypes = {}
tmp_dataframe = pd.read_csv(tmp_buffer.open(tmp_file),
                            usecols=used_cols,
                            )
