# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-22 04:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_auto_20160621_1555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='extractedelements',
            name='x1_coordinate',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='extractedelements',
            name='y1_coordinate',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
