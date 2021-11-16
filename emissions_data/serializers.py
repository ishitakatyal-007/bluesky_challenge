from rest_framework import serializers

from .models import GHGsEmissions

class EmissionSerializer(serializers.ModelSerializer):
    class Meta:
        db_table = GHGsEmissions
        fields = ("all", )