# Generated by Django 2.1.7 on 2019-04-02 17:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0013_user_time'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='time',
            new_name='timec',
        ),
    ]