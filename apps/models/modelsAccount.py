from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField

from apps.models.modelsProperty import Country, City, Region, Property


class MyUserManager(UserManager):
    def create_user(self, username, is_administrator=False, is_tenant=False, email=None, password=None, **kwargs):
        """Create and return a `User` with an email, phone number, username and password."""
        if username is None:
            raise TypeError('Users must have a username.')
        if email is None:
            raise TypeError('Users must have an email.')
        if is_administrator is False and is_tenant is False:
            raise TypeError('Users must have a role.')

        user = self.model(username=username, email=self.normalize_email(email), isTenant=is_tenant,
                          isAdministrator=is_administrator)
        user.set_password(password)
        user.save(using=self._db)
        if is_administrator:
            Administrator(user=user).save()
        if is_tenant:
            Tenant(user=user).save()

        return user


class User(AbstractUser):
    # username = models.CharField(_('Username'), blank=False, null=False, max_length=25)
    first_name = models.CharField(_('First Name of User'), blank=True, max_length=50)
    last_name = models.CharField(_('Last Name of User'), blank=True, max_length=50)
    email = models.EmailField(_("Email Address"), blank=True, null=True, default="")
    # USERNAME_FIELD = 'username'
    # REQUIRED_FIELDS = []
    isAdministrator = models.BooleanField(default=False)
    isTenant = models.BooleanField(default=False)
    isRealEstateAgent = models.BooleanField(default=False)
    userConnection = models.ManyToManyField("self", default=None, blank=True)
    objects = MyUserManager()

    class Meta:
        # managed = False
        db_table = 'auth_user'
        app_label = "Account"


class WorksWithAgents(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    worksWithAgents = models.BooleanField(default=False)
    receiveRecommendations = models.BooleanField(default=True)
    phone_number = PhoneNumberField(null=True, blank=True, verbose_name="Phone number")
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Date of birth")
    profile_picture = models.ImageField(null=True, blank=True, default=None)
    nationality = models.CharField(max_length=25, blank=True, default=None, null=True)

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
