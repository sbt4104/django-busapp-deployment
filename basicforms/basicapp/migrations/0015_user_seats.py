# Generated by Django 2.1.7 on 2019-04-02 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicapp', '0014_auto_20190402_1756'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='seats',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
