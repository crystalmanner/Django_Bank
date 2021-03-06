# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-24 21:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0060_fill_has_finished'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='is_public',
            field=models.BooleanField(verbose_name="This exam is publicly available for users who are not editors", default=True),
        ),
    ]
