from django.contrib import admin

from company.models import Catalog


@admin.register(Catalog)
class OrganizationModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', )
    # search_fields = ['name', ]