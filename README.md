# bluesky_challenge

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
