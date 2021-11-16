import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bluesky_challenge.settings')

django.setup()

data = 'data.csv'

from countries.models import Countries
from categories.models import EmissionCategories
from emissions_data.models import GHGsEmissions

class GHGEmissionData():

    @staticmethod
    def update_emission_data():

        with open(data, 'r') as file_countries:
            csv_reader = csv.reader(file_countries)          
            
            for record in csv_reader:
                country = record[0]
                year = record[1]
                category = record[3]
                value = record[2]            

                category_record = EmissionCategories.objects.filter(category_description=category).first()
                country_record = Countries.objects.filter(country_name=country).first()

                emission_record = GHGsEmissions.objects.filter(category_id=EmissionCategories.objects.filter(category_description=category).first(), country_id=Countries.objects.filter(country_name=country).first(), year=year, value=value).first()

                if not emission_record:
                    GHGsEmissions.objects.create(category_id=EmissionCategories.objects.filter(category_description=category).first(), country_id=Countries.objects.filter(country_name=country).first(), year=year, value=value).save()
                    print("Data added successfully to the DB....")
                    

if __name__ == "__main__":
    x = GHGEmissionData()
    x.update_emission_data()