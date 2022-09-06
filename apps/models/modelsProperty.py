from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
import datetime

from django import forms


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


class Property(models.Model):
    owner = models.ForeignKey("Account.Administrator", on_delete=models.CASCADE, blank=False, null=False)
    tenants = models.ManyToManyField("Account.Tenant", blank=True, default=None)
    location = models.ForeignKey(City, on_delete=models.DO_NOTHING, blank=True, null=False, default=None)
    usable_area = models.FloatField(default=0, blank=False, null=True)
    year = models.IntegerField(validators=[MinValueValidator(1984), max_value_current_year])
    currency_type = models.CharField(max_length=20, choices=[("EURO", "EURO"), ("RON", "RON")], default="RON")
    rent_price = models.FloatField(blank=True, null=True)
    selling_price = models.FloatField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Properties"
        app_label = "Property"


class PropertyPicture(models.Model):
    image = models.ImageField(height_field=150, width_field=150)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)


class MyForm(forms.ModelForm):
    year = forms.TypedChoiceField(coerce=int, choices=year_choices, initial=current_year)
