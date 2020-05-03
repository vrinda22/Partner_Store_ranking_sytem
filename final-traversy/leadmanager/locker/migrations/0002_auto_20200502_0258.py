# Generated by Django 3.0.5 on 2020-05-01 21:28

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('locker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onboard',
            name='name',
            field=models.CharField(max_length=250, validators=[django.core.validators.RegexValidator('^[a-z-A-Z ]+$', message='Numbers not allowed')]),
        ),
    ]