# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-01-02 15:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_profile_mangers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='personal_email_confirmation_key_created',
            field=models.DateTimeField(blank=True, null=True, verbose_name='creation date of alternative email confirmation key'),
        ),
    ]
