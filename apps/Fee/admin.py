from django.contrib import admin

from apps.models.modelsFee import *

admin.site.register([UtilityType, Provider, UtilityBill, Payment, Rent, Subscription])
