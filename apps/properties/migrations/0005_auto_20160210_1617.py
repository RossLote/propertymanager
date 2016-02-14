# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-10 16:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0004_property_year_built'),
    ]

    operations = [
        migrations.AlterField(
            model_name='property',
            name='attributes',
            field=models.ManyToManyField(blank=True, to='properties.PropertyAttribute'),
        ),
    ]
