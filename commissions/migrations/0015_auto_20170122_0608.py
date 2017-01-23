# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-01-22 06:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commissions', '0014_auto_20170122_0552'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LeaseOption',
            new_name='Option',
        ),
        migrations.RenameModel(
            old_name='LeaseTerm',
            new_name='Term',
        ),
        migrations.AlterModelOptions(
            name='option',
            options={'ordering': ('-expiration_date',)},
        ),
    ]