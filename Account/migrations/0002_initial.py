# Generated by Django 4.0.5 on 2022-06-24 16:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Property', '0001_initial'),
        ('Account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenanthistory',
            name='property',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Property.property'),
        ),
        migrations.AddField(
            model_name='tenanthistory',
            name='tenant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Account.tenant'),
        ),
        migrations.AddField(
            model_name='tenant',
            name='cityInterested',
            field=models.ManyToManyField(blank=True, default=None, to='Property.city'),
        ),
        migrations.AddField(
            model_name='tenant',
            name='countryInterested',
            field=models.ManyToManyField(blank=True, default=None, to='Property.country'),
        ),
        migrations.AddField(
            model_name='tenant',
            name='regionInterested',
            field=models.ManyToManyField(blank=True, default=None, to='Property.region'),
        ),
    ]