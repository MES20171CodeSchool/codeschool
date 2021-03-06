# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-01 13:04
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cs_activities', '0002_auto_20160504_1329_squashed_0017_auto_20160601_0908'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='finalresponse',
            options={'verbose_name': 'final response', 'verbose_name_plural': 'final responses'},
        ),
        migrations.AddField(
            model_name='finalresponse',
            name='final_grade',
            field=models.DecimalField(blank=True, decimal_places=3, help_text='Final grade given to activity considering all responses, penalties, etc.', max_digits=6, null=True, verbose_name='Final grade'),
        ),
        migrations.AlterField(
            model_name='finalresponse',
            name='activity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='final_responses', to='cs_activities.Activity'),
        ),
        migrations.AlterField(
            model_name='finalresponse',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='final_responses', to=settings.AUTH_USER_MODEL),
        ),
    ]
