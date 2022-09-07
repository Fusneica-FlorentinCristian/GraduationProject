from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
import datetime

from django import forms

# from apps.models.modelsAccount import Administrator, Tenant


def year_choices():
    return [(r, r) for r in range(1984, datetime.date.today().year+1)]


def current_year():
    return datetime.date.today().year


def max_value_current_year(value):
    return MaxValueValidator(current_year())(value)


class Country(models.Model):
    tag = models.CharField(max_length=3, primary_key=True, null=False, blank=False)
    name = models.CharField(max_length=30, blank=False, null=False)

    class Meta:
        verbose_name_plural = "Countries"
        app_label = "Property"

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=30, blank=False, null=False)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)

    class Meta:
        app_label = "Property"

    def __str__(self):
        return f'{self.name},  {self.country}'


class City(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, blank=False, null=False)

    class Meta:
        verbose_name_plural = "Cities"
        app_label = "Property"

    def __str__(self):
        return f'{self.name}, {self.region}'


class PropertyManager(models.Manager):
    def create_property(self, owner_user_id, city_id=None, currency_type="RON", tenant_user_ids=None, usable_area=0,
                        year=False, rent_price=None, selling_price=None):
        administrator = Property.owner.model.objects.filter(pk=owner_user_id).first()
        city = Property.location.model.objects.filter(pk=city_id).first()

        if administrator is None or owner_user_id is None:
            raise TypeError('Properties must have an owner.')

        estate = self.model(
            owner=administrator,
            tenants=Property.tenants.model.objects.filter(id__in=tenant_user_ids),
            location=city,
            usable_area=usable_area,
            year=year,
            currency_type=currency_type,
            rent_price=rent_price,
            selling_price=selling_price)

        estate.save()


class Property(models.Model):
    owner = models.ForeignKey("Account.Administrator", on_delete=models.CASCADE, blank=False, null=False)
    tenants = models.ManyToManyField("Account.Tenant", blank=True, default=[None])
    location = models.ForeignKey(City, on_delete=models.DO_NOTHING, blank=True, null=True, default=None)
    usable_area = models.FloatField(default=0, blank=False, null=False)
    year = models.IntegerField(validators=[MinValueValidator(1984), max_value_current_year], default=None, null=True, blank=True)
    currency_type = models.CharField(max_length=20, choices=[("EURO", "EURO"), ("RON", "RON")], default="RON")
    rent_price = models.FloatField(blank=True, null=True)
    selling_price = models.FloatField(blank=True, null=True)

    objects = PropertyManager

    class Meta:
        verbose_name_plural = "Properties"
        app_label = "Property"


class PropertyPicture(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="Property/", default=None, null=True,
                              height_field=150, width_field=150)


class MyForm(forms.ModelForm):
    year = forms.TypedChoiceField(coerce=int, choices=year_choices, initial=current_year)
