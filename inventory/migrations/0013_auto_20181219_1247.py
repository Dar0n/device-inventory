# Generated by Django 2.1.4 on 2018-12-19 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0012_auto_20181219_1039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='device',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='inventory.Device'),
        ),
    ]