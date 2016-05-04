# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-20 01:07
from __future__ import unicode_literals

from django.db import migrations
import model_utils.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cs_activities', '0002_auto_20160419_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='status_changed',
        ),
        migrations.AlterField(
            model_name='activity',
            name='status',
            field=model_utils.fields.StatusField(choices=[(0, 'dummy')], default='open', max_length=100, no_check_for_status=True, verbose_name=(('open', 'open'), ('closed', 'closed'), ('draft', 'draft'))),
        ),
    ]