SQL Assignment
Choose a nursing home ("Facility"), and subset the data by that nursing home. Answer the following using SQL.


Question 1:  The count of how many censuses were reported
YOUR QUERY: select count(*) from beds where Facility_ID = 17;
QUERY RESULTS: 220



Question 2:  Find the earliest census date
YOUR QUERY: select Bed_Census_Date from beds where Facility_ID = 17 order by Bed_Census_Date limit 1;
QUERY RESULTS: 01/02/2013



Question 3:  Find the latest census date
YOUR QUERY: select Bed_Census_Date from beds where Facility_ID = 17 order by Bed_Census_Date DESC limit 1;
QUERY RESULTS: 12/30/2009



Question 4:  Find the ten census dates with the highest number of available beds for that nursing home
YOUR QUERY: select Bed_Census_Date from beds where FAcility_ID =17 order by Available_Residential_Beds limit 10;
QUERY RESULTS:
Bed_Census_Date
07/21/2010
02/01/2012
01/18/2012
10/24/2012
01/25/2012
12/22/2010
09/29/2010
01/20/2010
07/08/2009
09/26/2012


Question 5:  Find the ten census dates with the lowest number of available beds for that nursing home
YOUR QUERY: select Bed_Census_Date from beds where FAcility_ID =17 order by Available_Residential_Beds DESC limit 10;
QUERY RESULTS:
Bed_Census_Date
04/10/2013
11/09/2011
01/02/2013
11/07/2012
08/29/2012
12/26/2012
06/20/2012
05/22/2013
01/23/2013
05/16/2012

update beds
  set new_dates =
  select substr(t.Bed_Census_Date, 7) || substr(t.Bed_Census_Date, 1, 2) || substr(t.Bed_Census_Date, 4, 5)
  from beds as t
  where t.id = beds.id;
