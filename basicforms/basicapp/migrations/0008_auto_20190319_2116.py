# Generated by Django 2.1.5 on 2019-03-19 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0007_auto_20190319_2115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ml_data',
            name='delay',
            field=models.TimeField(default='20:00'),
        ),
    ]
