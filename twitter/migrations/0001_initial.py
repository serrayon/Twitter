
# Generated by Django 2.2.4 on 2019-08-09 22:54


import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.CharField(default='', max_length=140)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(default='', max_length=140)),


                ('photo_url', models.CharField(default='', max_length=250)),
                ('date', models.DateTimeField(default=datetime.datetime(2019, 8, 9, 18, 4, 20, 261815, tzinfo=utc))),

                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='posts', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(default='', max_length=140)),

               
                ('date', models.DateTimeField(default=datetime.datetime(2019, 8, 9, 18, 4, 20, 262312, tzinfo=utc))),

                ('post', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='comments_post', to='twitter.Post')),
                ('user', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='comments_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
