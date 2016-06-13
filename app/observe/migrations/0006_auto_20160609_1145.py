# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-09 11:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('observe', '0005_auto_20160608_1252'),
    ]

    operations = [
        migrations.RenameField(
            model_name='request',
            old_name='asteroids',
            new_name='asteroid',
        ),
        migrations.AlterField(
            model_name='asteroid',
            name='end',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 9, 11, 45, 30, 303022)),
        ),
        migrations.AlterField(
            model_name='asteroid',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 9, 11, 45, 30, 302789)),
        ),
        migrations.AlterField(
            model_name='request',
            name='email',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('P', 'Pending'), ('C', 'Completed'), ('S', 'Scheduled')], max_length=1),
        ),
        migrations.AlterField(
            model_name='request',
            name='twitter',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='update_time',
            field=models.DateTimeField(default=datetime.datetime(2016, 6, 9, 11, 45, 30, 304142)),
        ),
    ]