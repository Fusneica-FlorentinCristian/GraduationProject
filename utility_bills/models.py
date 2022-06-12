from django.contrib.auth.models import User
from django.db import models


class UtilityType(models.Model):
    name = models.CharField(max_length=50)


class Provider(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(UtilityType, verbose_name='utility type', on_delete=models.DO_NOTHING)


class Bill(models.Model):
    is_payed = models.BooleanField(default=False)
    post_date = models.DateTimeField(verbose_name='Bill added', auto_now_add=True)
    bill_deadline = models.DateField(verbose_name='due date', blank=True, default=None, null=True)
    value = models.FloatField()
    payee_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="payee")
    propriety_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="propriety_owner")
    provider = models.ForeignKey(Provider, on_delete=models.DO_NOTHING)
    file = models.FileField(blank=True, default=None, null=True)


class Payment(models.Model):
    payment_date = models.DateTimeField(verbose_name='Payment date')
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
