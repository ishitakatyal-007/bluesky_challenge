from django.db import models

# Create your models here.
from django_extensions.db.models import TimeStampedModel

class EmissionCategories(TimeStampedModel):
    category_id = models.AutoField(
        primary_key=True,
        help_text="Emission category",
        verbose_name="Emission Category",
        )
    category_description = models.TextField(
        help_text="Category description",
        verbose_name="Category Decription",
        )
    category_alias = models.CharField(
        max_length=10,
        null=True,
        blank=True,
        help_text="Alias for category",
        verbose_name="Category Alias",
        )

    def __str__(self):
        return str(self.category_id) + "--" + self.category_description + "--" + str(self.category_alias)

    class Meta:
        db_table = "emission_categories"
        verbose_name = "Emission Categorie"
        ordering = ("created", )

