# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-14 21:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('properties', '0008_auto_20160211_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='property',
        ),
        migrations.RemoveField(
            model_name='document',
            name='team',
        ),
        migrations.DeleteModel(
            name='Document',
        ),
    ]
