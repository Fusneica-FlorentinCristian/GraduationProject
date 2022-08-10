from django.contrib import admin

# Register your models here.
from apps.models.modelsProperty import City, Country, Property, Region

admin.site.register([Property, City, Country, Region])
