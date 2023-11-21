import sqlite3
import pathlib
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy import stats

def Locate_Filepath(path:str)->pathlib.WindowsPath:
    '''Returns the full file path, from an input of the file location relative to the parent project folder'''
    current_file_path = pathlib.Path(__file__).parent.resolve()
    base_folder = current_file_path.parents[0]
    full_path = base_folder.joinpath(path)
    return full_path

def Database_To_Dataframe(database_path:pathlib.WindowsPath, table_in:str, columns:str)->pd.DataFrame:
    '''returns a dataframe given the database filepath, database table name, and columns to return'''
    db_conn = sqlite3.connect(database_path)
    df = pd.read_sql_query(f'SELECT {columns} FROM {table_in}', db_conn)
    db_conn.close()
    return df

def Plot_Histogram(data:pd.Series, bins:list):
    plt.hist(data, bins=bins)
    plt.show()
    return

def Show_Colourbar(bounds:list,cmap:mpl.colors.ListedColormap):
    fig, ax = plt.subplots(figsize=(6,1), layout='constrained')
    norm = mpl.colors.BoundaryNorm(bounds, cmap.N)
    fig.colorbar(mpl.cm.ScalarMappable(norm=norm, cmap=cmap),
                cax=ax, orientation='vertical', spacing='uniform')
    plt.show()

if __name__=="__main__":
    # Retrieve Data
    database_path = Locate_Filepath('2. Data\\Database\\nrdp_fare_data.db')
    flow_fare_loc_df = Database_To_Dataframe(database_path, "flow_fare_location", "FLOW_ID, POUND_PER_MILE")
    # Calculate quintiles
    bin_edges = stats.mstats.mquantiles(flow_fare_loc_df["POUND_PER_MILE"], [0.2, 0.4, 0.6, 0.8])
    print(bin_edges)
    # Create Histogram to visualise quintiles
    Plot_Histogram(flow_fare_loc_df["POUND_PER_MILE"], [0,0.85,1.2,1.7,2.6,20])
    #Plot quintiles on scatter plot
    Show_Colourbar([0,0.85,1.2,1.7,2.6,20], mpl.cm.magma)