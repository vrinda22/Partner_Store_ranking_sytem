# Generated by Django 3.0.5 on 2020-05-01 21:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Onboard',
            fields=[
                ('lockerid', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]+$', message='Numbers not allowed')])),
                ('country', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]+$', message='Numbers not allowed')])),
                ('address', models.TextField()),
                ('zipcode', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^\\d{1,10}$', message='Only numbers are allowed'), django.core.validators.MinLengthValidator(6)])),
                ('total_slots', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Throughput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('throughput', models.FloatField()),
                ('lockerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locker.Onboard')),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('lockerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locker.Onboard')),
            ],
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('non_del_days', models.CharField(default='0000000', max_length=7, validators=[django.core.validators.RegexValidator('^\\d{1,10}$', message='Letters not permissible'), django.core.validators.MinLengthValidator(7)], verbose_name='Non delivery days')),
                ('timings_open', models.TimeField()),
                ('timings_closed', models.TimeField()),
                ('status', models.BooleanField()),
                ('lockerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locker.Onboard')),
            ],
        ),
        migrations.CreateModel(
            name='Rankinglist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rank', models.IntegerField()),
                ('name', models.CharField(max_length=250, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]+$', message='Numbers not allowed')])),
                ('country', models.CharField(max_length=100, validators=[django.core.validators.RegexValidator('^[a-zA-Z ]+$', message='Numbers not allowed')])),
                ('address', models.TextField()),
                ('zipcode', models.CharField(max_length=6, validators=[django.core.validators.RegexValidator('^\\d{1,10}$', message='Only numbers are allowed'), django.core.validators.MinLengthValidator(6)])),
                ('non_del_days', models.CharField(default='0000000', max_length=7, validators=[django.core.validators.RegexValidator('^\\d{1,10}$', message='Letters not permissible'), django.core.validators.MinLengthValidator(7)], verbose_name='Non delivery days')),
                ('timings_open', models.TimeField()),
                ('timings_closed', models.TimeField()),
                ('status', models.BooleanField()),
                ('lockerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locker.Onboard')),
            ],
            options={
                'unique_together': {('lockerid', 'rank')},
            },
        ),
        migrations.CreateModel(
            name='Occupancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('occupancy', models.FloatField()),
                ('lockerid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='locker.Onboard')),
            ],
            options={
                'unique_together': {('lockerid', 'date')},
            },
        ),
    ]
