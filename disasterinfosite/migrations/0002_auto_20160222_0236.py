# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.contrib.gis.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('disasterinfosite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EQ_Fault_Buffer',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='EQ_Fault_Shaking',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='EQ_Fault_Worst',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='EQ_Historic_Distance',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Fire_Burn_Potential',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('lookup_val', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Fire_Hist_Bound',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Fire_Worst_Case_placeholder',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Flood_Channel_Migration_Zones',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Flood_FEMA_DFRIM_2015',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('femades', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Flood_Worst_Case',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Landslide_placeholder2',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('lookup_val', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='summerstorm',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='winterstorm',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQ_Fault_Buffer_filter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, null=True, to='disasterinfosite.EQ_Fault_Buffer', related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQ_Fault_Shaking_filter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, null=True, to='disasterinfosite.EQ_Fault_Shaking', related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQ_Fault_Worst_filter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, null=True, to='disasterinfosite.EQ_Fault_Worst', related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQ_Historic_Distance_filter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, null=True, to='disasterinfosite.EQ_Historic_Distance', related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Fire_Burn_Potential_filter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, null=True, to='disasterinfosite.Fire_Burn_Potential', related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Fire_Hist_Bound_filter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, null=True, to='disasterinfosite.Fire_Hist_Bound', related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Fire_Worst_Case_placeholder_filter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, null=True, to='disasterinfosite.Fire_Worst_Case_placeholder', related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Flood_Channel_Migration_Zones_filter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, null=True, to='disasterinfosite.Flood_Channel_Migration_Zones', related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Flood_FEMA_DFRIM_2015_filter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, null=True, to='disasterinfosite.Flood_FEMA_DFRIM_2015', related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Flood_Worst_Case_filter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, null=True, to='disasterinfosite.Flood_Worst_Case', related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Landslide_placeholder2_filter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, null=True, to='disasterinfosite.Landslide_placeholder2', related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='summerstorm_filter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, null=True, to='disasterinfosite.summerstorm', related_name='+', blank=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='winterstorm_filter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, null=True, to='disasterinfosite.winterstorm', related_name='+', blank=True),
        ),
    ]
