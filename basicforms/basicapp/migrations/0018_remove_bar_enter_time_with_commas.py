# Generated by Django 2.1.7 on 2019-04-03 08:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0017_auto_20190403_0748'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bar',
            name='enter_time_with_commas',
        ),
    ]
