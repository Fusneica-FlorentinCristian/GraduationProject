from django.contrib import admin
from Account.models import *
from django.contrib.auth.admin import UserAdmin


admin.site.register(User, UserAdmin)
admin.site.register([Administrator, Tenant, TenantHistory])
# Register your models here.
