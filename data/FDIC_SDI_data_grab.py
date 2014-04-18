"""
Grabs the entire Federal Deposit Insurance Corporation (FDIC) Statistics on 
Depository Institutions (SDI) data set.

"""
# built-in Python libraries
import os, StringIO, zipfile

import pandas as pd
import requests

base_url = 'http://www2.fdic.gov/SDI/Resource/AllReps/All_Reports_'

# use pandas to construct a list of quarterly dates
present = '20131231'
datetimes = pd.date_range('19921231', end=present, freq='Q')
dates = datetimes.format(formatter=lambda t: t.strftime('%Y%m%d'))

# construct the url...
tmp_date = dates[0]
tmp_url = base_url + tmp_date + '.zip'

# ...make the connection and grab the zipped files...
tmp_buffer = requests.get(tmp_url)

# ...unzip the files...
tmp_zipped_files = StringIO.StringIO(tmp_buffer.content)
tmp_unzipped_files = zipfile.ZipFile(tmp_zipped_files)

# ...and finally extract results!
tmp_dir = 'All_Reports_' + tmp_date
os.mkdir(tmp_dir)
tmp_unzipped_files.extractall(path=tmp_dir)