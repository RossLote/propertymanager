# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-14 22:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deleted_at', models.DateTimeField(blank=True, default=None, editable=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('object_id', models.PositiveIntegerField()),
                ('title', models.CharField(blank=True, default=None, max_length=200, null=True, verbose_name='title')),
                ('file', models.FileField(upload_to='documents', verbose_name='File')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType')),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='teams.Team')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
