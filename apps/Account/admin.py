from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.Account.models import User, Administrator, Tenant, TenantHistory

admin.site.register(User, UserAdmin)
admin.site.register([Administrator, Tenant, TenantHistory])
# Register your models here.
