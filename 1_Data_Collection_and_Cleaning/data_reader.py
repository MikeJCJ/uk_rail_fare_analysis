############################################################################################################################
# This script extracts the rail data from its raw foramt, and converts the file to a csv which can be imported into SQLite #
############################################################################################################################

import pandas as pd
import pathlib

#Data files' information to be extracted
flow_data_path = '2. Data\RailFareData\RJFAF775.ffl'
flow_table_name= 'flow_data'
flow_code_length = 49
flow_data_cols=[
    ['ORIGIN_CODE',2,6],
    ['DESTINATION_CODE',6,10],
    ['ROUTE_CODE',10,15],
    ['STATUS_CODE',15,18],
    ['USAGE_CODE',18,19],
    ['DIRECTION',19,20],
    ['END_DATE',20,28],
    ['START_DATE',28,36],
    ['TOC',36,39],
    ['CROSS_LONDON_IND',39,40],
    ['NS_DISC_IND',40,41],
    ['PUBLICATION_IND',41,42],
    ['FLOW_ID',42,49]
]

fare_data_path = '2. Data\RailFareData\RJFAF775.ffl'
fare_table_name= 'fare_data'
fare_code_length = 22
fare_data_cols=[
    ['FLOW_ID',2,9],
    ['TICKET_CODE',9,12],
    ['FARE',12,20],
    ['RESTRICTION_CODE',20,22]
]


#Retrieving base folder path
current_file_path = pathlib.PurePath(__file__)
base_folder = current_file_path.parents[1]
output_path = base_folder.joinpath('2. Data\CleanedData')

#Converting NRDP file to CSV
def ConvertNRDPtoCSV(data_path:str, data_cols:str, table_name:str, code_length:int):
    ''' This function takes in the file path, column structure, and desired
    table name for the NRDP data file, and outputs as a csv to be directly
    inputted into SQLiteStudio'''
    full_data_path = base_folder.joinpath(data_path)
    output_path = base_folder.joinpath(f'2. Data\CleanedData\{table_name}.csv')
    data_df = pd.read_csv(full_data_path, skiprows=6, names=['FULL_CODE']).query(f"FULL_CODE.str.len()=={code_length}")
    i=0
    while i<len(data_cols):
        data_df[data_cols[i][0]] = data_df['FULL_CODE'].str[data_cols[i][1]:data_cols[i][2]]
        i+=1
    data_df.to_csv(output_path, index=False)
    return data_df


if __name__=="__main__":
    flow_data_df = ConvertNRDPtoCSV(flow_data_path, flow_data_cols, flow_table_name, flow_code_length)
    fare_data_df = ConvertNRDPtoCSV(fare_data_path, fare_data_cols, fare_table_name, fare_code_length)
    print(fare_data_df)
