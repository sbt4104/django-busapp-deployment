# Generated by Django 2.1.7 on 2019-04-03 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0019_bar_enter_time_with_commas'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bar',
            old_name='enter_time_with_commas',
            new_name='enter_time',
        ),
    ]
