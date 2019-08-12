# Generated by Django 2.2.4 on 2019-08-10 22:50

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('twitter', '0002_auto_20190809_1804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 10, 22, 50, 35, 688311, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 8, 10, 22, 50, 35, 687732, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='photo_url',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
