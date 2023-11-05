import pandas as pd
import pathlib

# Options

# Retrieving base folder path
current_file_path = pathlib.PurePath(__file__)
base_folder = current_file_path.parents[1]
station_coords_file_path = base_folder.joinpath('2. Data\StationCoords\stations.csv')
output_path = base_folder.joinpath(f'2. Data\CleanedData\station_coords.csv')

# Importing csv to pd
station_coords_df = pd.read_csv(station_coords_file_path, delimiter=';')
station_coords_df = station_coords_df.loc[station_coords_df['country']=='GB']
station_coords_df = station_coords_df.loc[:, station_coords_df.columns.isin(['id','name','slug','uic','latitude','longitude','parent_station_id','is_city','is_main_station','is_airport','main_station_hint','same_as'])]
station_coords_df.to_csv(output_path, index=False)
