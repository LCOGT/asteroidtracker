# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2018-06-21 07:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('observe', '0016_auto_20180620_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asteroid',
            name='last_update',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='observation',
            name='last_update',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
