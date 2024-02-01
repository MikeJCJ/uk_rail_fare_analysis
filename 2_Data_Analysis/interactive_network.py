import sqlite3
import pathlib
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib as mpl
from pyproj import Transformer

def setup():
    #Setup mercator projection
    transformer = Transformer.from_crs("EPSG:4326","esri:54030")
    # Locating files
    base_folder = pathlib.Path().resolve()
    database_path = base_folder.joinpath('2. Data\\Database\\nrdp_fare_data.db')
    return database_path, transformer

def read_data(database_path):
    # reading database table into a dataframe
    db_conn = sqlite3.connect(database_path)
    df = pd.read_sql_query('SELECT * FROM flow_fare_location', db_conn)
    db_conn.close()
    return df

def project_latlon_mercator(input_coords:tuple, transformer=None)->tuple:
    ''' This function takes in a set of lon/lat coordinates and
    performs the mercator projection on them, in order to display them correctly
    on a map'''
    if type(transformer) == None:
        raise ValueError("Transformer has not been assigned")
    lon = input_coords[0]
    lat = input_coords[1]
    x,y = transformer.transform(lon, lat)
    output_coords = (y,x)
    return output_coords

def transform_data(flow_fare_loc_df:pd.DataFrame, transformer):
    flow_fare_loc_df['ORIGIN_COORDS'] = list(zip(flow_fare_loc_df.ORIGIN_LON,flow_fare_loc_df.ORIGIN_LAT))
    flow_fare_loc_df['DESTINATION_COORDS'] = list(zip(flow_fare_loc_df.DESTINATION_LON,flow_fare_loc_df.DESTINATION_LAT))
    network_df = flow_fare_loc_df[['ORIGIN_CODE','DESTINATION_CODE','FARE_POUNDS','ORIGIN_COORDS','DESTINATION_COORDS','POUND_PER_MILE']].copy()
    network_df['ORIGIN_COORDS'] = network_df['ORIGIN_COORDS'].apply(project_latlon_mercator, transformer=transformer)
    network_df['DESTINATION_COORDS'] = network_df['DESTINATION_COORDS'].apply(project_latlon_mercator, transformer=transformer)
    network_df['COST_RANK'] = pd.qcut(network_df['POUND_PER_MILE'],5,labels=False)
    return network_df

def create_graph(network_df:pd.DataFrame):
    # Create list of station and routes (with route stats) from the network_df
    stations = {}
    routes = []
    for i in range(len(network_df)):
        stations[network_df['ORIGIN_CODE'][i]]=network_df['ORIGIN_COORDS'][i]
        stations[network_df['DESTINATION_CODE'][i]]=network_df['DESTINATION_COORDS'][i]
        routes.append((network_df['ORIGIN_CODE'][i],network_df['DESTINATION_CODE'][i],network_df['COST_RANK'][i]))

    #Create graph from station and route data
    G = nx.Graph()
    for i in range(len(routes)):
        G.add_edge(stations[routes[i][0]],stations[routes[i][1]],weight=routes[i][2])
    pos = {value:value for key, value in stations.items()} # Creates nodes in graph
    return G

if __name__ == "__main__":
    flow_fare_loc_database_path, transformer = setup()
    flow_fare_loc_df =read_data(flow_fare_loc_database_path)
    network_df = transform_data(flow_fare_loc_df, transformer)
    G = create_graph(network_df)