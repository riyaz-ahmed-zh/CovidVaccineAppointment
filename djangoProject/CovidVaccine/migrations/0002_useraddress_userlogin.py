# Generated by Django 3.2.1 on 2021-05-15 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CovidVaccine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAddress',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('street', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('zipcode', models.IntegerField()),
                ('locationx', models.IntegerField()),
                ('locationy', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Userlogin',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
            ],
        ),
    ]
