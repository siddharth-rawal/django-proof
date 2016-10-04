# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=140, null=True, blank=True)),
                ('phonenumber', models.IntegerField(null=True, blank=True)),
                ('gender', models.CharField(max_length=140, null=True, blank=True)),
                ('profile_picture', models.ImageField(null=True, upload_to=b'photos', blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_profile',
            },
            bases=(models.Model,),
        ),
    ]
