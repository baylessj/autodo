# Generated by Django 2.2.12 on 2020-05-25 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('mileage', models.FloatField()),
                ('numRefuelings', models.IntegerField(default=0)),
                ('averageEfficiency', models.FloatField()),
                ('distanceRate', models.FloatField()),
                ('lastMileageUpdate', models.DateTimeField()),
                ('make', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('year', models.IntegerField()),
                ('plate', models.CharField(max_length=10)),
                ('vin', models.CharField(max_length=10)),
                ('imageName', models.CharField(max_length=255)),
            ],
        ),
    ]
