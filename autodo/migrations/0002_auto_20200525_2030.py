# Generated by Django 2.2.12 on 2020-05-25 20:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('autodo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OdomSnapshot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('mileage', models.FloatField()),
            ],
        ),
        migrations.RemoveField(
            model_name='car',
            name='averageEfficiency',
        ),
        migrations.RemoveField(
            model_name='car',
            name='distanceRate',
        ),
        migrations.RemoveField(
            model_name='car',
            name='lastMileageUpdate',
        ),
        migrations.RemoveField(
            model_name='car',
            name='mileage',
        ),
        migrations.RemoveField(
            model_name='car',
            name='numRefuelings',
        ),
        migrations.AddField(
            model_name='car',
            name='color',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('dueMileage', models.FloatField()),
                ('dueDate', models.DateTimeField()),
                ('estimatedDueDate', models.BooleanField(default=False)),
                ('mileageRepeatInterval', models.FloatField()),
                ('daysRepeatInterval', models.IntegerField()),
                ('monthsRepeatInterval', models.IntegerField()),
                ('yearsRepeatInterval', models.IntegerField()),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autodo.Car')),
                ('completionOdomSnapshot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autodo.OdomSnapshot')),
            ],
        ),
        migrations.CreateModel(
            name='Refueling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.IntegerField()),
                ('amount', models.FloatField()),
                ('odomSnapshot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autodo.OdomSnapshot')),
            ],
        ),
        migrations.AddField(
            model_name='odomsnapshot',
            name='car',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='autodo.Car'),
        ),
    ]
