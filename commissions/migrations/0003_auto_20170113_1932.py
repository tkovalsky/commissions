# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-13 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0002_auto_20170113_1929'),
    ]

    operations = [
        migrations.RenameField(
            model_name='lease',
            old_name='house_salesrep_commission_rate',
            new_name='house_broker_commission_rate',
        ),
        migrations.AddField(
            model_name='lease',
            name='house_broker',
            field=models.CharField(blank=True, max_length=80),
        ),
    ]