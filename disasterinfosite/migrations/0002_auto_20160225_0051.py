# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.contrib.gis.db.models.fields
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('disasterinfosite', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EQ_Fault_Buffer',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='EQ_Fault_Shaking',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='EQ_Fault_Worst',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='EQ_Historic_Distance',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Fire_Burn_Probability2',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Fire_Hist_Bound2',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Fire_Worst_Case_ph2',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Flood_Channel_Migration_Zones',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('lookup_val', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Flood_FEMA_DFRIM_2015',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('femades', models.CharField(max_length=80)),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Flood_Worst_Case',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='Landslide_placeholder2',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('lookup_val', models.FloatField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='summerstorm',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.CreateModel(
            name='winterstorm',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('lookup_val', models.IntegerField()),
                ('geom', django.contrib.gis.db.models.fields.MultiPolygonField(srid=4326)),
            ],
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQ_Fault_Buffer_filter',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.EQ_Fault_Buffer', null=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQ_Fault_Shaking_filter',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.EQ_Fault_Shaking', null=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQ_Fault_Worst_filter',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.EQ_Fault_Worst', null=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='EQ_Historic_Distance_filter',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.EQ_Historic_Distance', null=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Fire_Burn_Probability2_filter',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.Fire_Burn_Probability2', null=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Fire_Hist_Bound2_filter',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.Fire_Hist_Bound2', null=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Fire_Worst_Case_ph2_filter',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.Fire_Worst_Case_ph2', null=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Flood_Channel_Migration_Zones_filter',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.Flood_Channel_Migration_Zones', null=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Flood_FEMA_DFRIM_2015_filter',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.Flood_FEMA_DFRIM_2015', null=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Flood_Worst_Case_filter',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.Flood_Worst_Case', null=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='Landslide_placeholder2_filter',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.Landslide_placeholder2', null=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='summerstorm_filter',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.summerstorm', null=True),
        ),
        migrations.AddField(
            model_name='snugget',
            name='winterstorm_filter',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='disasterinfosite.winterstorm', null=True),
        ),
    ]
