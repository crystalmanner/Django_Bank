# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-10 15:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teams', '0005_team_exams'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='team',
            name='categories',
        ),
    ]
