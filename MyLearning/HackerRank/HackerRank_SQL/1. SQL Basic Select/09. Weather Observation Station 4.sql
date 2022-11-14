/*
OUTPUT:
difference total number city and number city distinct
*/

SELECT (COUNT(city)-COUNT(DISTINCT city))       #total number city - total distinct city
FROM station