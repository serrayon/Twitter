# Generated by Django 2.2.4 on 2019-08-12 20:41

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0004_auto_20190810_2328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 12, 20, 41, 9, 876989, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 12, 20, 41, 9, 876418, tzinfo=utc)),
        ),
    ]