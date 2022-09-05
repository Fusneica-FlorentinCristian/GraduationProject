# Generated by Django 4.0.5 on 2022-09-05 22:46

import apps.models.modelsAccount
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0003_user_phone_number_alter_administrator_iscollaborator_and_more'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', apps.models.modelsAccount.MyUserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='user',
            name='isAdministrator',
        ),
        migrations.RemoveField(
            model_name='user',
            name='isRealEstateAgent',
        ),
        migrations.RemoveField(
            model_name='user',
            name='isTenant',
        ),
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='user',
            name='userConnection',
        ),
        migrations.AddField(
            model_name='administrator',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Date of birth'),
        ),
        migrations.AddField(
            model_name='administrator',
            name='isAdministrator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='administrator',
            name='isRealEstateAgent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='administrator',
            name='isTenant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='administrator',
            name='nationality',
            field=models.CharField(blank=True, default=None, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='administrator',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Phone number'),
        ),
        migrations.AddField(
            model_name='administrator',
            name='profile_picture',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='administrator',
            name='userConnection',
            field=models.ManyToManyField(blank=True, default=None, to='Account.administrator'),
        ),
        migrations.AddField(
            model_name='tenant',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True, verbose_name='Date of birth'),
        ),
        migrations.AddField(
            model_name='tenant',
            name='isAdministrator',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tenant',
            name='isRealEstateAgent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tenant',
            name='isTenant',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tenant',
            name='nationality',
            field=models.CharField(blank=True, default=None, max_length=25, null=True),
        ),
        migrations.AddField(
            model_name='tenant',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Phone number'),
        ),
        migrations.AddField(
            model_name='tenant',
            name='profile_picture',
            field=models.ImageField(blank=True, default=None, null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='tenant',
            name='userConnection',
            field=models.ManyToManyField(blank=True, default=None, to='Account.tenant'),
        ),
    ]
