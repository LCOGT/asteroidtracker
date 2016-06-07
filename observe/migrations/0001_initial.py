# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-07 13:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asteroid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=15, null=True, verbose_name='Designation')),
                ('source_type', models.CharField(blank=True, choices=[('N', 'NEO'), ('A', 'Asteroid'), ('C', 'Comet'), ('K', 'KBO'), ('E', 'Centaur'), ('T', 'Trojan'), ('U', 'Candidate'), ('X', 'Did not exist'), ('W', 'Was not interesting'), ('D', 'Discovery, non NEO'), ('J', 'Artificial satellite')], max_length=1, null=True, verbose_name='Type of object')),
                ('elements_type', models.CharField(blank=True, choices=[('MPC_MINOR_PLANET', 'MPC Minor Planet'), ('MPC_COMET', 'MPC Comet')], max_length=16, null=True, verbose_name='Elements type')),
                ('active', models.BooleanField(default=False, verbose_name='Actively following?')),
                ('epochofel', models.DateTimeField(blank=True, null=True, verbose_name='Epoch of elements')),
                ('orbinc', models.FloatField(blank=True, null=True, verbose_name='Orbital inclination in deg')),
                ('longascnode', models.FloatField(blank=True, null=True, verbose_name='Longitude of Ascending Node (deg)')),
                ('argofperih', models.FloatField(blank=True, null=True, verbose_name='Arg of perihelion (deg)')),
                ('eccentricity', models.FloatField(blank=True, null=True, verbose_name='Eccentricity')),
                ('meandist', models.FloatField(blank=True, help_text='for asteroids', null=True, verbose_name='Mean distance (AU)')),
                ('meananom', models.FloatField(blank=True, help_text='for asteroids', null=True, verbose_name='Mean Anomaly (deg)')),
                ('perihdist', models.FloatField(blank=True, help_text='for comets', null=True, verbose_name='Perihelion distance (AU)')),
                ('epochofperih', models.DateTimeField(blank=True, help_text='for comets', null=True, verbose_name='Epoch of perihelion')),
                ('arc_length', models.FloatField(blank=True, null=True, verbose_name='Length of observed arc (days)')),
                ('exposure', models.IntegerField(default=0)),
                ('filter_name', models.CharField(max_length=10)),
                ('start', models.DateTimeField(default=datetime.datetime(2016, 6, 7, 13, 28, 14, 394047))),
                ('end', models.DateTimeField(default=datetime.datetime(2016, 6, 7, 13, 28, 14, 394252))),
                ('instrument', models.CharField(max_length=30)),
                ('aperture', models.CharField(max_length=3)),
                ('binning', models.IntegerField(default=2)),
                ('information', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('track_num', models.CharField(max_length=10)),
                ('status', models.CharField(max_length=1)),
                ('update_time', models.DateTimeField(blank=True, null=True)),
                ('email', models.CharField(max_length=150)),
                ('twitter', models.CharField(max_length=15)),
                ('asteroids', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='observe.Asteroid')),
            ],
        ),
    ]