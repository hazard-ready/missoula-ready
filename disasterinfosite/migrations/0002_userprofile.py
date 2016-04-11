# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('disasterinfosite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('address1', models.CharField(max_length=200, blank=True)),
                ('address2', models.CharField(max_length=200, blank=True)),
                ('city', models.CharField(max_length=200, blank=True)),
                ('state', models.CharField(max_length=50, blank=True)),
                ('zip_code', models.CharField(max_length=50, blank=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Profile',
            },
        ),
    ]
