# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-02 13:48
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exams', '0025_clean_up_session_fields'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='is_answer',
            new_name='is_right',
        ),
        migrations.RemoveField(
            model_name='session',
            name='marked',
        ),
        migrations.RemoveField(
            model_name='session',
            name='right_answers',
        ),
        migrations.RemoveField(
            model_name='session',
            name='solved',
        ),
        migrations.AddField(
            model_name='question',
            name='marking_users',
            field=models.ManyToManyField(blank=True, related_name='marked_questions', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='session',
            name='is_solved',
            field=models.BooleanField(default=False, verbose_name='Show question solved?'),
        ),
        migrations.AlterField(
            model_name='session',
            name='number_of_questions',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='question_filter',
            field=models.CharField(choices=[('UNUSED', 'Unused'), ('INCORRECT', 'Incorrect'), ('MARKED', 'Marked'), ('ALL', 'All')], default=None, max_length=20),
        ),
        migrations.AlterField(
            model_name='session',
            name='questions',
            field=models.ManyToManyField(blank=True, to='exams.Question'),
        ),
        migrations.AlterField(
            model_name='session',
            name='subjects',
            field=models.ManyToManyField(blank=True, to='exams.Subject'),
        ),
    ]
