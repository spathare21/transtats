# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-11-06 10:59
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20171009_0910'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reports',
            fields=[
                ('reports_id', models.AutoField(primary_key=True, serialize=False)),
                ('report_subject', models.CharField(max_length=200, unique=True)),
                ('report_json', django.contrib.postgres.fields.jsonb.JSONField(null=True)),
                ('report_updated', models.DateTimeField(null=True)),
            ],
            options={
                'verbose_name': 'Reports',
                'db_table': 'ts_reports',
            },
        ),
    ]
