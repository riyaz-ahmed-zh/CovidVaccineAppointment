# Generated by Django 3.2.1 on 2021-05-16 01:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CovidVaccine', '0011_auto_20210515_1852'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='prioritydate',
            table='prioritydate',
        ),
        migrations.AlterModelTable(
            name='user',
            table='user',
        ),
        migrations.AlterModelTable(
            name='useraddress',
            table='useraddress',
        ),
        migrations.AlterModelTable(
            name='userlogin',
            table='userlogin',
        ),
    ]
