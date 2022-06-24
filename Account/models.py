from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from Property.models import Country, City, Region, Property


class User(AbstractUser):
    first_name = models.CharField(_('First Name of User'), blank=True, max_length=50)
    last_name = models.CharField(_('Last Name of User'), blank=True, max_length=50)
    email = models.EmailField(_("Email Address"), blank=True, null=True, default="")
    isManager = models.BooleanField(default=False)
    isTenant = models.BooleanField(default=False)
    isRealEstateAgent = models.BooleanField(default=False)
    userConnection = models.ManyToManyField("self", default=None, blank=True)
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'auth_user'


class WorksWithAgents(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    worksWithAgents = models.BooleanField(default=True)
    receiveRecommendations = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Manager(WorksWithAgents):
    isCollaborator = models.BooleanField(default=False)
    isOwner = models.BooleanField(default=False)


class Tenant(WorksWithAgents):
    countryInterested = models.ManyToManyField(Country, blank=True, default=None)
    regionInterested = models.ManyToManyField(Region, blank=True, default=None)
    cityInterested = models.ManyToManyField(City, blank=True, default=None)


class TenantHistory(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.DO_NOTHING)
    property = models.ForeignKey(Property, on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True, default=None, blank=True)

    class Meta:
        verbose_name_plural = "TenantHistories"
