# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 12:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cs_activities', '0016_auto_20160531_2328'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='ResponseGroup',
            new_name='FinalResponse',
        ),
    ]
