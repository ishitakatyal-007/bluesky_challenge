from django.db import models

# Create your models here.
from django_extensions.db.models import TimeStampedModel

from categories.models import EmissionCategories
from countries.models import Countries

class GHGsEmissions(TimeStampedModel):
    data_id = models.AutoField(
        primary_key=True,
        help_text="unique value for data",
        verbose_name="GHGs Emissions ID",
        )
    category_id = models.ForeignKey(
        "categories.EmissionCategories",
        on_delete=models.CASCADE,
        help_text="Foreign key relation to Categories model",
        verbose_name="Emission category",
        )
    country_id = models.ForeignKey(
        "countries.Countries",
        on_delete=models.CASCADE,
        help_text="Foreign key relation to Countries model",
        verbose_name="Counrties",
        )
    year = models.IntegerField(
        help_text="Year",
        verbose_name="Year",
        )
    value = models.FloatField(
        help_text="value of GHG emissions",
        verbose_name="Emissions value",
        )

    def __str__(self):
        return str(self.country_id) + ": " + str(self.year) + " -- " + str(self.value)

    class Meta:
        db_table = "ghg_emission_data"
        verbose_name = "GHGs Emission Data"
        ordering = ("year", )