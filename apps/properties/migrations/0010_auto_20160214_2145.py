# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-14 21:45
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0009_auto_20160214_2137'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='property',
            options={'verbose_name_plural': 'properties'},
        ),
    ]
