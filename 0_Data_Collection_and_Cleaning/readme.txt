The below steps outline to the process in order to collect all of the relevant data for this project across the various data sources.

1 - Data extraction:
    1a - Firstly the rail flow (station-to-station route) and fare data are obtained from the NRDP data portal, which is accessed via an API as described by nrdp_data_collection_instructions.
        - This data is converted into a csv format using the data_reader.py script.
    1b - The station to lat/lon coordinate lookup is obtained by using the data provided in the following data repository: https://github.com/trainline-eu/stations.
        - This data is processed using the data_reader_station_coords.py script.
    1c - The station links data (data with distances between adjacent stations) is comma delimited, and can be imported into excel to save as a csv. Found from routing data file: RJRG0769.RGD
    1d - The conversion between different station codes can be found in the file "RJRG0769.RGY". This is comma delimited, and can be imported into excel to save as a csv.
2 - This data is then uploaded to a local SQLiteStudio database for analysis. The import_data_fixes.sql script must be run in order to fix formatting issues when importing the data.
3 - data_cleaning_code.sql must be run to remove duplicates from the fare table.
