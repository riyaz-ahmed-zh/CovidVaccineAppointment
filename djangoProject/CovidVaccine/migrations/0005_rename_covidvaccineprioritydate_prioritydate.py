# Generated by Django 3.2.1 on 2021-05-16 01:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CovidVaccine', '0004_auto_20210515_1829'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CovidvaccinePriorityDate',
            new_name='PriorityDate',
        ),
    ]
