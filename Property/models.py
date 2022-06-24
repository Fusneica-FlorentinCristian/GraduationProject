from django.db import models

# Create your models here.
# import Account.models


class Country(models.Model):
    tag = models.CharField(max_length=3, primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=30, blank=False, null=False)

    class Meta:
        verbose_name_plural = "Countries"


class Region(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class City(models.Model):
    country = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=False, null=False)

    class Meta:
        verbose_name_plural = "Cities"


class Property(models.Model):
    owner = models.ForeignKey("Account.Manager", on_delete=models.CASCADE, blank=False, null=False)
    tenants = models.ManyToManyField("Account.Tenant", blank=True, default=None)
    location = models.ForeignKey(City, on_delete=models.DO_NOTHING, blank=True, null=False, default=None)

    class Meta:
        verbose_name_plural = "Properties"

