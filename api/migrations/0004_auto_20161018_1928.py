# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-10-18 23:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20161018_1447'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_id',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='begin_time',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='meeting',
            name='end_time',
            field=models.TimeField(),
        ),
    ]
