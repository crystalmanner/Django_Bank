# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-12 07:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0050_session_is_deleted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Highlight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highlighted_text', models.TextField()),
                ('submission_date', models.DateTimeField(auto_now_add=True, null=True)),
                ('revision', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.Revision')),
                ('session', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='exams.Session')),
                ('stricken_choices', models.ManyToManyField(blank=True, related_name='striking_answers', to='exams.Choice')),
            ],
        ),
        migrations.RemoveField(
            model_name='answer',
            name='is_marked',
        ),
    ]