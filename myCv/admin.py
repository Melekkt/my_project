from django.contrib import admin
from myCv.models import *


@admin.register(GeneralSetting)
# Register your models here.
class GeneralSettingAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'description', 'parameters', 'updated_date', 'created_date']
    search_fields = ['name','description','parameters']
    list_editable = ['description','parameters']

    class Meta:
        model = GeneralSetting
