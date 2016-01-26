# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-26 15:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('teams', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('deleted_at', models.DateTimeField(blank=True, default=None, editable=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.PositiveSmallIntegerField(choices=[(10, 'Mr'), (20, 'Miss'), (30, 'Mrs'), (40, 'Ms')])),
                ('forename', models.CharField(max_length=40)),
                ('middlenames', models.CharField(blank=True, max_length=150)),
                ('surname', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='landlords', to='teams.Team')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Tenant',
            fields=[
                ('deleted_at', models.DateTimeField(blank=True, default=None, editable=False, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name='modified')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.PositiveSmallIntegerField(choices=[(10, 'Mr'), (20, 'Miss'), (30, 'Mrs'), (40, 'Ms')])),
                ('forename', models.CharField(max_length=40)),
                ('middlenames', models.CharField(blank=True, max_length=150)),
                ('surname', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(max_length=128)),
                ('team', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tenants', to='teams.Team')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
