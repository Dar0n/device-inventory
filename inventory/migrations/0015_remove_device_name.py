# Generated by Django 2.1.4 on 2018-12-19 15:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0014_auto_20181219_1306'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='device',
            name='name',
        ),
    ]
