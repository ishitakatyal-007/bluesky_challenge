import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bluesky_challenge.settings')

django.setup()

data = 'categories.txt'

from categories.models import EmissionCategories

class UpdateCategroies():

    @staticmethod
    def update_categories():

        with open(data, 'r') as file_categories:
            categories = file_categories.read()

            for category in categories.replace(",", "").split("\n"):
                # print(category)
                category_record = EmissionCategories.objects.filter(category_description=category).first()

                if not category_record:
                    EmissionCategories.objects.create(category_description=category).save()
                    print(category, 'added to the database..')

if __name__ == "__main__":
    x = UpdateCategroies()
    x.update_categories()