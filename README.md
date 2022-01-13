# bluesky_challenge
TASK:
Taking this dataset from Kaggle - https://www.kaggle.com/unitednations/international-greenhouse-gas-emissions

You have to clean this dataset as per the needs mentioned below and store it in any database of your choice (you can use SQLite (file based) as data won't change for this assignment)

You have to build the following APIs :

/countries - get all countries in the dataset (names, ids and their possible values for startYear and endYear)
/country/id?queries=explained-below
temporal queries - startYear | endYear
parameters queries - one or parameters (e.g, CO2 or CO2 and NO2)
should return all values for the selected parameters between startYear and endYear
Add appropriate checks for queries and erroneous values

SOLUTION:

The url is: https://www.ghg-emissions.herokuapp.com
The following urls in the specified format are accessible:
1.  https://ghg-emissions.herokuapp.com/ : This takes you to a login panel. 
username: admin 
password: admin123
** First visit the admin site to check for the database tables and also see the aliases for the emission criteria to be used further...
2. https://www.ghg-emissions.herokuapp.com/countries/ : This prints the {country_name_1 : {start_year: 1990, end_year:2014}, country_name_2 : {}}
3. https://www.ghg-emissions.herokuapp.com/countries/2/N2O,CO2/ : This prints the value of ghg_emissions for country_id=2 and ghg_criteria=[N2O, CO2]
4. https://www.ghg-emissions.herokuapp.com/countries/2/1997/2005/ : This prints the value of ghg_emissions for country_id=2 and year in range=[1997 to 2005]
5. https://www.ghg-emissions.herokuapp.com/countries/2/1997/2005/N2O,HFCs/: This prints the value of ghg_emissions for country_id=2 and year in range=[1997 to 2005]  for ghg_criteria=[N2O, HFCs]
** Website caching has been developed.
** Code is written in python-django
**You can play around with the numbers and the data too.. So do as you will....

Hoping to hear from you soon! Hope you'll like it...
