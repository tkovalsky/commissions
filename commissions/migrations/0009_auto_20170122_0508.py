# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 05:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0008_location_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='tenant',
            name='locations',
            field=models.ManyToManyField(blank=True, to='commissions.Location'),
        ),
        migrations.RemoveField(
            model_name='location',
            name='tenants',
        ),
        migrations.AddField(
            model_name='location',
            name='tenants',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='commissions.Tenant'),
        ),
    ]
