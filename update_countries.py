import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bluesky_challenge.settings')

django.setup()

data = 'countries.txt'

from countries.models import Countries

class UpdateCountries():

    @staticmethod
    def update_countries():

        with open(data, 'r') as file_countries:
            countries = file_countries.read()

            for country in countries.replace(",", "").split("\n"):
                country_record = Countries.objects.filter(country_name=country).first()

                if not country_record:
                    Countries.objects.create(country_name=country).save()
                    print(country, 'added to the database..')
                    pass

if __name__ == "__main__":
    x = UpdateCountries()
    x.update_countries()