#######################
Rail Network Analysis #
#######################

Key Skills: Clustering Algorithms | Visualising Networks | Database Creation | APIs 

-----------
- Process -
-----------

UK Rail Analysis Project which consists of these main stages:
    1 - Data Collection through the National Rail Data Portal (NRDP) API, and other sources.
    2 - Data Warehouse Creation.
    3 - Data Analysis Performed

Stage 1 - Data Collection
    - The stages of retrieving the rail data via the NRDP API are detaileed in data_collection_instructions.sh. Through this the rail fare data for all uk rail routes is gathered.
    - The rail fare and route data are cleaned and converted to csvs using the data_reader.py script and these csvs are imported into sqlite studio.

Stage 2 - Data Warehouse Creation
    - The fare data has to be cleaned using the script fare_data_import_fix.sql
		- Various other data sources are added to this SQLite database.
		- Views can be created such as the Flow_Fare_location view which has each possible train journey, the cost, and location of the stations.

Stage 3 - Analysis
		- exploratory analysis of the data in order to determine best visualisations.
		- Route cost view mapped using networkx library with matplotlib.
		- Clustering Analysis of routes
