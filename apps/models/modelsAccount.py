from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

from apps.models.modelsProperty import Country, City, Region, Property


class MyUserManager(UserManager):
    def create_user(self, username, isAdministrator=False, isTenant=False, email=None, password=None, **kwargs):
        """Create and return a `User` with an email, phone number, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email.')
        if isAdministrator is False and isTenant is False:
            raise TypeError('Users must have a role.')

        user = self.model(username=username, email=self.normalize_email(email), isTenant=isTenant,
                          isAdministrator=isAdministrator)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, username, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')
        if email is None:
            raise TypeError('Superusers must have an email.')
        if username is None:
            raise TypeError('Superusers must have an username.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractUser):
    # username = models.CharField(_('Username'), blank=False, null=False, max_length=25)
    first_name = models.CharField(_('First Name of User'), blank=True, max_length=50)
    last_name = models.CharField(_('Last Name of User'), blank=True, max_length=50)
    email = models.EmailField(_("Email Address"), blank=True, null=True, default="")
    isAdministrator = models.BooleanField(default=False)
    isTenant = models.BooleanField(default=False)
    isRealEstateAgent = models.BooleanField(default=False)
    userConnection = models.ManyToManyField("self", default=None, blank=True)
    # USERNAME_FIELD = 'username'
    phone_number = PhoneNumberField(null=True, blank=True, verbose_name="Phone number")
    # REQUIRED_FIELDS = []
    objects = MyUserManager()

    class Meta:
        # managed = False
        db_table = 'auth_user'
        app_label = "Account"


class WorksWithAgents(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    worksWithAgents = models.BooleanField(default=False)
    receiveRecommendations = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

    class Meta:
        abstract = True


class Administrator(WorksWithAgents):
    isCollaborator = models.BooleanField("Collaborates with other administrators", default=False)
    isOwner = models.BooleanField("Has properties", default=False)

    class Meta:
        app_label = "Account"


class Enterprise(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        app_label = "Account"


class IBAN(models.Model):
    code = models.CharField(max_length=24, primary_key=True)
    user = models.ForeignKey(Administrator, on_delete=models.CASCADE, blank=True, null=True)
    enterprise = models.ForeignKey(Enterprise, on_delete=models.DO_NOTHING, null=True, blank=True)

    class Meta:
        app_label = "Account"


class Tenant(WorksWithAgents):
    countryInterested = models.ManyToManyField(Country, blank=True, default=None)
    regionInterested = models.ManyToManyField(Region, blank=True, default=None)
    cityInterested = models.ManyToManyField(City, blank=True, default=None)

    class Meta:
        app_label = "Account"

    # def __str__(self):
    #     representation = ''
    #     representation += f"{[region for region in self.regionInterested]}"
    #     representation += f"{[region for region in self.regionInterested]}"
    #     representation += f"{[region for region in self.regionInterested]}"
    #     return self.name


class TenantHistory(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.DO_NOTHING)
    property = models.ForeignKey(Property, on_delete=models.DO_NOTHING)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True, default=None, blank=True)

    class Meta:
        verbose_name_plural = "TenantHistories"
        app_label = "Account"


# class UserManager(BaseUserManager):
#     def create_user(self, username, email, password=None, **kwargs):
#         """Create and return a `User` with an email, phone number, username and password."""
#         if username is None:
#             raise TypeError('Users must have a username.')
#         if email is None:
#             raise TypeError('Users must have an email.')
#
#         user = self.model(username=username, email=self.normalize_email(email))
#         user.set_password(password)
#         user.save(using=self._db)
#
#         return user
#
#     def create_superuser(self, username, email, password):
#         """
#         Create and return a `User` with superuser (admin) permissions.
#         """
#         if password is None:
#             raise TypeError('Superusers must have a password.')
#         if email is None:
#             raise TypeError('Superusers must have an email.')
#         if username is None:
#             raise TypeError('Superusers must have an username.')
#
#         user = self.create_user(username, email, password)
#         user.is_superuser = True
#         user.is_staff = True
#         user.save(using=self._db)
#
#         return user
