from django.contrib import admin
from Fee.models import *


admin.register([UtilityType, Provider, UtilityBill, Payment, Rent, Subscription, Payment])
