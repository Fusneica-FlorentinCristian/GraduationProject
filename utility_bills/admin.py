from django.contrib import admin
from utility_bills.models import *


admin.register([UtilityType, Provider, Bill, Payment])