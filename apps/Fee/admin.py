from django.contrib import admin

from apps.Fee.models import *

admin.site.register([UtilityType, Provider, UtilityBill, Payment, Rent, Subscription])
