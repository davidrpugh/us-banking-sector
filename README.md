# The size distribution of U.S. banks

Python code for replicating the statistical analysis from my paper on the evolution of the U.S. bank size distribution.

## `data`

Folder contains two scripts:

1. `FDIC_SDI_data_grab.py`: Python script that grabs the entire FDIC SDI database and downloads it (compressed!) into the working directory.
2. `FDIC_SDI_data_wrangling.py`: Python script that constructs a Pandas Panel object out of a subset of the SDI data set. 

 