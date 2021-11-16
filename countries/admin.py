from django.contrib import admin

# Register your models here.
from .models import Countries

class CountriesAdmin(admin.ModelAdmin):
    list_display = ["country_name", ]
    
    def has_add_permissions(self, request, obj=None):
        return True
    
    def has_delete_permissions(self, request, obj=None):
        return True
    
    def has_change_permissions(self, request, obj=None):
        return True

admin.site.register(Countries, CountriesAdmin)