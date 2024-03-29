# Generated by Django 4.0.5 on 2022-08-10 15:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Property', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isPayed', models.BooleanField(default=False)),
                ('post_date', models.DateTimeField(auto_now_add=True, verbose_name='Bill added')),
                ('deadline', models.DateField(blank=True, default=None, null=True, verbose_name='due date')),
                ('balance', models.FloatField(default=0.0, null=True)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_%(app_label)s.%(class)s_set+', to='contenttypes.contenttype')),
            ],
        ),
        migrations.CreateModel(
            name='UtilityType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.ManyToManyField(to='Fee.utilitytype')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_date', models.DateTimeField(verbose_name='Payment date')),
                ('status_message', models.CharField(default='', max_length=20, null=True)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Fee.fee')),
            ],
        ),
        migrations.CreateModel(
            name='UtilityBill',
            fields=[
                ('fee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Fee.fee')),
                ('file', models.FileField(default=None, null=True, upload_to='Fee/UtilityBill')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Property.property')),
                ('provider', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Fee.provider')),
                ('type', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='Fee.utilitytype')),
            ],
            bases=('Fee.fee',),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('fee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Fee.fee')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('Fee.fee',),
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('fee_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='Fee.fee')),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='Property.property')),
            ],
            bases=('Fee.fee',),
        ),
    ]
