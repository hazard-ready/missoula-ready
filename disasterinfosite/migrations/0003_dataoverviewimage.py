# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disasterinfosite', '0002_auto_20160226_0335'),
    ]

    operations = [
        migrations.CreateModel(
            name='DataOverviewImage',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('link_text', models.CharField(max_length=100, default='')),
                ('image', models.ImageField(upload_to='data')),
            ],
        ),
    ]
