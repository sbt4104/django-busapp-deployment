# Generated by Django 2.1.5 on 2019-03-19 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0008_auto_20190319_2116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ml_data',
            name='delay',
            field=models.TextField(default='20:00'),
        ),
    ]
