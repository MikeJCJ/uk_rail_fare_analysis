/*
# Data Importing Fixes #
*/

-- 1. Fare Data fix
UPDATE fare_data_20230829
SET RESTRICTION_CODE = SUBSTRING(FULL_CODE,21,2)
;

UPDATE fare_data_20230829
SET RESTRICTION_CODE = NULL
WHERE RESTRICTION_CODE = '  '
;

-- 2. Station Coords fix
UPDATE station_coords
SET uic = SUBSTR(uic,1,7)