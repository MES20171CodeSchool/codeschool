# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 02:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cs_activities', '0014_auto_20160531_2238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='activity',
            old_name='grading_method_object',
            new_name='grading_method',
        ),
    ]
