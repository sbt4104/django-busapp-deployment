# Generated by Django 2.1.5 on 2019-03-19 21:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0009_auto_20190319_2119'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ml_data',
            name='delay',
        ),
    ]
