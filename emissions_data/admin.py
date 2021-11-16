from django.contrib import admin

# Register your models here.
from .models import GHGsEmissions

class EmissionsDataAdmin(admin.ModelAdmin):
    list_display = ["year", "country", "category", "value"]
    list_filter = ["year", "country_id",]

    def category(self, obj):
        x = str(obj.category_id).split("--")[2]
        return x

    def country(self, obj):
        x = str(obj.country_id).split("--")[1]
        return x

    def has_add_permissions(self, request, obj=None):
        return True
    
    def has_delete_permissions(self, request, obj=None):
        return True
    
    def has_change_permissions(self, request, obj=None):
        return True

admin.site.register(GHGsEmissions, EmissionsDataAdmin)