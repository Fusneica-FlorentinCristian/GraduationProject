from django.db import models
from polymorphic.models import PolymorphicModel

from apps.models.modelsProperty import Property
from django.conf import settings


class UtilityType(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        app_label = "Fee"

    def __str__(self):
        return self.name


class Provider(models.Model):
    name = models.CharField(max_length=100)
    type = models.ManyToManyField(UtilityType)

    class Meta:
        app_label = "Fee"

    def __str__(self):
        return self.name


class Fee(PolymorphicModel):
    isPayed = models.BooleanField(default=False)
    post_date = models.DateTimeField(verbose_name='Bill added', auto_now_add=True)
    deadline = models.DateField(verbose_name='due date', blank=True, default=None, null=True)
    balance = models.FloatField(null=True, default=0.0)

    class Meta:
        app_label = "Fee"


class UtilityBill(Fee):
    type = models.ForeignKey(UtilityType, on_delete=models.DO_NOTHING, default=None, null=True)
    file = models.FileField(upload_to="Fee/UtilityBill", default=None, null=True)
    provider = models.ForeignKey(Provider, on_delete=models.DO_NOTHING, default=None, null=True)
    property = models.ForeignKey(Property, on_delete=models.DO_NOTHING)

    class Meta:
        app_label = "Fee"


class Rent(Fee):
    property = models.ForeignKey(Property, on_delete=models.DO_NOTHING)

    class Meta:
        app_label = "Fee"


class Subscription(Fee):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.DO_NOTHING)

    class Meta:
        app_label = "Fee"


class Payment(models.Model):
    payment_date = models.DateTimeField(verbose_name='Payment date')
    status_message = models.CharField(max_length=20, null=True, default="")
    bill = models.ForeignKey(Fee, on_delete=models.CASCADE)

    class Meta:
        app_label = "Fee"
