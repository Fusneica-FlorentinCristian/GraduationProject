# Generated by Django 4.0.5 on 2022-06-24 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Fee', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fee',
            old_name='value',
            new_name='balance',
        ),
    ]