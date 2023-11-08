-- This query creates a view that has each flow, their stations names, and location for single adult fares
SELECT
    T1.FLOW_ID,
    T4.TICKET_CODE,
    T1.ORIGIN_CODE,
    T1.DESTINATION_CODE,
    T2.name AS ORIGIN_NAME,
    T3.name AS DESTINATION_NAME,
    T2.latitude AS ORIGIN_LAT,
    T2.longitude AS ORIGIN_LON,
    T3.latitude AS DESTINATION_LAT,
    T3.longitude AS DESTINATION_LON,
    CAST(T4.FARE AS FLOAT)/100 AS FARE_POUNDS

FROM flow_data_20230829 T1

LEFT JOIN station_coords T2 --ORIGIN STATIONS
ON T1.ORIGIN_CODE=SUBSTR(T2.uic,3,4)

LEFT JOIN station_coords T3 --DESTINATION STATIONS
ON T1.DESTINATION_CODE=SUBSTR(T3.uic,3,4)

LEFT JOIN fare_data_20230829 T4
ON T1.FLOW_ID=T4.FLOW_ID

WHERE ORIGIN_NAME IS NOT NULL
    AND DESTINATION_NAME IS NOT NULL
    AND TICKET_CODE = 'SDS' --Anytime Day Single
;