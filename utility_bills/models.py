from datetime import date

from django.contrib.auth.models import User
from django.db import models


class UtilityType(models.Model):
    name = models.CharField(max_length=50)


class Provider(models.Model):
    name = models.CharField(max_length=100)
    type = models.ManyToManyField(UtilityType)


class Bill(models.Model):
    is_payed = models.BooleanField(default=False)
    post_date = models.DateTimeField(verbose_name='Bill added', auto_now_add=True)
    bill_deadline = models.DateField(verbose_name='due date', blank=True, default=None, null=True)
    value = models.FloatField(null=True, default=0.0)
    tenants = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="payee", null=True, default=None)
    property_owner = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="propriety_owner_user")
    provider = models.ForeignKey(Provider, on_delete=models.DO_NOTHING, default=None, null=True)
    type = models.ForeignKey(UtilityType, on_delete=models.DO_NOTHING, default=None, null=True)
    file = models.FileField(upload_to="Fee", default=None, null=True)


class Payment(models.Model):
    payment_date = models.DateTimeField(verbose_name='Payment date')
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
