from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from Property.models import Country, City, Region, Property


class User(AbstractUser):
    # username = models.CharField(_('Username'), blank=False, null=False, max_length=25)
    first_name = models.CharField(_('First Name of User'), blank=True, max_length=50)
    last_name = models.CharField(_('Last Name of User'), blank=True, max_length=50)
    email = models.EmailField(_("Email Address"), blank=True, null=True, default="")
    isAdministrator = models.BooleanField(default=False)
    isTenant = models.BooleanField(default=False)
    isRealEstateAgent = models.BooleanField(default=False)
    userConnection = models.ManyToManyField("self", default=None, blank=True)
    USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = []

    class Meta:
        db_table = 'auth_user'


class WorksWithAgents(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    worksWithAgents = models.BooleanField(default=False)
    receiveRecommendations = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        abstract = True


class Administrator(WorksWithAgents):
    # username = models.CharField(default=None, max_length=50)
    isCollaborator = models.BooleanField(default=False)
    isOwner = models.BooleanField(default=False)
    # username = self.user.username


class Enterprise(models.Model):
    name = models.CharField(max_length=50)


class IBAN(models.Model):
    code = models.CharField(max_length=24, primary_key=True)
    user = models.ForeignKey(Administrator, on_delete=models.CASCADE, blank=False, null=False)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.DO_NOTHING)


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
