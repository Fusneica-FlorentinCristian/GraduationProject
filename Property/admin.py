from django.contrib import admin
from Property.models import *

# Register your models here.


admin.site.register([Property, City, Country, Region])