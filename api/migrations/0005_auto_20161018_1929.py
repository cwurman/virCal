# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-18 23:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_auto_20161018_1928'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meeting',
            name='begin_time',
            field=models.TimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='end_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
