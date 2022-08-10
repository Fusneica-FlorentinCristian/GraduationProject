from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.models.modelsAccount import User, Administrator, Tenant, TenantHistory

admin.site.register(User, UserAdmin)
admin.site.register([Administrator, Tenant, TenantHistory])
# Register your models here.
