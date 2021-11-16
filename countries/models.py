from django.db import models

# Create your models here.
from django_extensions.db.models import TimeStampedModel

class Countries(TimeStampedModel):
    country_id = models.AutoField(
        primary_key=True,
        help_text="Unique ID for country",
        verbose_name="Country Unique ID",
        )
    country_name = models.CharField(
        max_length=100,
        help_text="Country name",
        verbose_name="Name of the country",
        )

    def __str__(self):
        return str(self.country_id) + "--" + self.country_name 

    class Meta:
        db_table = "countries"
        verbose_name = "Countrie"
        ordering = ("country_name", )
