# Generated by Django 2.1.7 on 2019-05-17 18:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0033_remove_ml_data_time_of_day'),
    ]

    operations = [
        migrations.AddField(
            model_name='ml_data',
            name='time_of_day',
            field=models.TimeField(default=datetime.datetime.today),
        ),
    ]
