from django.contrib.auth.models import User
from django.db import models


class UtilityType(models.Model):
    name = models.CharField(max_length=50)


class Provider(models.Model):
    name = models.CharField(max_length=100)
    type = models.ForeignKey(UtilityType, verbose_name='utility type', on_delete=models.DO_NOTHING)


# def bill_file_path(instance, filename) -> str:
#     return f"utility_bills/owner_{instance.propriety_owner_user.id}/payee_{instance.payee_user.id}/{filename}"


class Bill(models.Model):
    is_payed = models.BooleanField(default=False)
    post_date = models.DateTimeField(verbose_name='Bill added', auto_now_add=True)
    bill_deadline = models.DateField(verbose_name='due date', blank=True, default=None, null=True)
    value = models.FloatField(null=True)
    payee_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="payee", null=True, default=None)
    propriety_owner_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="propriety_owner_user")
    provider = models.ForeignKey(Provider, on_delete=models.DO_NOTHING)
    file = models.FileField(upload_to="utility_bills", default=None, null=True)


class Payment(models.Model):
    payment_date = models.DateTimeField(verbose_name='Payment date')
    bill = models.ForeignKey(Bill, on_delete=models.CASCADE)
