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
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='EQ_Historic_Distance',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='EQ_Most_Like',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('lookup_val', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='EQ_Worst_Case',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('lookup_val', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Fire_Hist_Bound',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Fire_Intensity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Fire_Worst_Case_placeholder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Flood_Channel_Migration_Zones',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Flood_FEMA_DFRIM_2015',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('femades', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Flood_Worst_Case_ph',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Landslide_placeholder',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('lookup_val', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQ_Fault_Buffer_filter',
            field=models.ForeignKey(blank=True, to='disasterinfosite.EQ_Fault_Buffer', on_delete=django.db.models.deletion.PROTECT, null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQ_Historic_Distance_filter',
            field=models.ForeignKey(blank=True, to='disasterinfosite.EQ_Historic_Distance', on_delete=django.db.models.deletion.PROTECT, null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQ_Most_Like_filter',
            field=models.ForeignKey(blank=True, to='disasterinfosite.EQ_Most_Like', on_delete=django.db.models.deletion.PROTECT, null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQ_Worst_Case_filter',
            field=models.ForeignKey(blank=True, to='disasterinfosite.EQ_Worst_Case', on_delete=django.db.models.deletion.PROTECT, null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Fire_Hist_Bound_filter',
            field=models.ForeignKey(blank=True, to='disasterinfosite.Fire_Hist_Bound', on_delete=django.db.models.deletion.PROTECT, null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Fire_Intensity_filter',
            field=models.ForeignKey(blank=True, to='disasterinfosite.Fire_Intensity', on_delete=django.db.models.deletion.PROTECT, null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Fire_Worst_Case_placeholder_filter',
            field=models.ForeignKey(blank=True, to='disasterinfosite.Fire_Worst_Case_placeholder', on_delete=django.db.models.deletion.PROTECT, null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Flood_Channel_Migration_Zones_filter',
            field=models.ForeignKey(blank=True, to='disasterinfosite.Flood_Channel_Migration_Zones', on_delete=django.db.models.deletion.PROTECT, null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Flood_FEMA_DFRIM_2015_filter',
            field=models.ForeignKey(blank=True, to='disasterinfosite.Flood_FEMA_DFRIM_2015', on_delete=django.db.models.deletion.PROTECT, null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Flood_Worst_Case_ph_filter',
            field=models.ForeignKey(blank=True, to='disasterinfosite.Flood_Worst_Case_ph', on_delete=django.db.models.deletion.PROTECT, null=True, related_name='+'),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Landslide_placeholder_filter',
            field=models.ForeignKey(blank=True, to='disasterinfosite.Landslide_placeholder', on_delete=django.db.models.deletion.PROTECT, null=True, related_name='+'),
        ),
    ]
