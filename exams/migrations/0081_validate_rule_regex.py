# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-21 07:44
from __future__ import unicode_literals

from django.db import migrations, models
import exams.models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0080_better_duplicate_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='regex_pattern',
            field=models.CharField(max_length=120, validators=[exams.models.validate_regex]),
        ),
    ]
