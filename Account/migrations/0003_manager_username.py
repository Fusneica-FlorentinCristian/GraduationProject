# Generated by Django 4.0.5 on 2022-06-24 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='manager',
            name='username',
            field=models.CharField(default='self.WorksWithAgent.user.username', max_length=50),
        ),
    ]
