from django.contrib.auth.models import User
from django.db import models


class Property(models.Model):
    owner = models.ForeignKey(User, on_delete=models.DO_NOTHING)
