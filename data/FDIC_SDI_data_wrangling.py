"""
This script imports the subset of the FDIC SDI data used in the analysis, 
converts the data to a Pandas data frame and writes the object to disk.

There are on the order of 50 corrupted observations in the various zip files.
Not clear why there are 90 entries in those rows instead of 89

"""
# built-in Python libraries
from datetime import datetime
import glob, zipfile

import pandas as pd

# use pandas to construct a list of quarterly dates
present = '20131231'
datetimes = pd.date_range('19921231', end=present, freq='Q')

# get a list of zip files over which to iterate
zip_files = glob.glob('*.zip')

# only want to return a subset of cols (save on memory usage!)
used_columns = ['cert', 'repdte', 'asset', 'lnlsnet', 'liab', 'dep', 'eqtot', 'numemp']
used_dtypes = {'cert':int, 'repdte':datetime, 'asset':float, 'lnlsnet':float, 
              'liab':float, 'eqtot':float, 'dep':float, 'numemp':float}

# create a container for the individual dataframes
dataframes = []

for zip_file in zip_files:

    tmp_buffer = zipfile.ZipFile(zip_file)
    
    # want to work with the assets and liabilities file
    tmp_file = tmp_buffer.namelist()[5]
    
    tmp_dataframe = pd.read_csv(tmp_buffer.open(tmp_file), 
                                index_col=['cert', 'repdte'],
                                error_bad_lines=False, # skips the mangled obs!
                                usecols=used_columns,
                                dtype=used_dtypes,
                                parse_dates=True,
                                )
                                                     
    dataframes.append(tmp_dataframe)
    
    print('Done with ' + zip_file + '!')
    
# concatenate the quarterly dataframes into a single data frame
combined_dataframe = pd.concat(dataframes)

# convert to panel (major_axis: cert, minor_axis: repdte)
combined_panel = combined_dataframe.to_panel()

# pickle the object for later use!
combined_panel.to_pickle('FDIC_SDI_panel.pkl')
