# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-11 04:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0013_auto_20170111_0357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='option',
            name='lease',
        ),
        migrations.AddField(
            model_name='lease',
            name='option',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='commissions.Option'),
        ),
    ]