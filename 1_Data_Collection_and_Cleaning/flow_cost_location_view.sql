SELECT
    T4.FLOW_ID,
    T5.TICKET_CODE,
    T2.NLC_CODE AS ORIGIN_CODE,
    T3.NLC_CODE AS DESTINATION_CODE,
    T6.name AS ORIGIN_NAME,
    T7.name AS DESTINATION_NAME,
    T6.latitude AS ORIGIN_LAT,
    T6.longitude AS ORIGIN_LON,
    T7.latitude AS DESTINATION_LAT,
    T7.longitude AS DESTINATION_LON,
    CAST(T5.FARE AS FLOAT)/100 AS FARE_POUNDS,
    T1.DISTANCE,
    (CAST(T5.FARE AS FLOAT)/100)/CAST(T1.DISTANCE AS FLOAT) AS POUND_PER_MILE

FROM station_links_20230829 T1 --Station to Station direct links
LEFT JOIN station_code_lookup T2
ON T1.ORIGIN_STATION=T2.CRS_CODE

LEFT JOIN station_code_lookup T3 --Station code lookup
ON T1.DESTINATION_STATION=T3.CRS_CODE

LEFT JOIN flow_data_20230829 T4 --Station to Station flow ID lookup
ON T2.NLC_CODE=T4.ORIGIN_CODE
    AND T3.NLC_CODE=T4.DESTINATION_CODE
    
LEFT JOIN fare_data_cleaned T5 --Fare data linked to routes through flow ID
ON T4.FLOW_ID=T5.FLOW_ID

LEFT JOIN station_coords T6 --ORIGIN STATIONS' NAMES
ON T2.NLC_CODE=SUBSTR(T6.uic,3,4)

LEFT JOIN station_coords T7 --DESTINATION STATIONS' NAMES
ON T3.NLC_CODE=SUBSTR(T7.uic,3,4)


WHERE T4.FLOW_ID IS NOT NULL
    AND TICKET_CODE='SDS' --Anytime Day Single
;