# Generated by Django 2.1.7 on 2019-07-27 11:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0037_auto_20190727_1139'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='Seats',
            new_name='seats',
        ),
    ]
