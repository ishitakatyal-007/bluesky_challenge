from django.contrib import admin

# Register your models here.
from .models import EmissionCategories

class EmissionCategoriesAdmin(admin.ModelAdmin):
    list_display = ["category_alias", "category_description"]
    list_filter = ["category_alias", ]

    def has_add_permissions(self, request, obj=None):
        return True

    def has_delete_permissions(self, request, obj=None):
        return True

    def has_change_permissions(self, request, obj=None):
        return True

admin.site.register(EmissionCategories, EmissionCategoriesAdmin)
