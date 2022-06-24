from django.contrib import admin
from Fee.models import *


admin.site.register([UtilityType, Provider, UtilityBill, Payment, Rent, Subscription])
