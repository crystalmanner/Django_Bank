# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-26 06:41
from __future__ import unicode_literals

from django.db import migrations


def add_exams(apps, schema_editor):
    Exam = apps.get_model('exams', 'Exam')
    Question = apps.get_model('exams', 'Question')

    for exam in Exam.objects.all():
        Question.objects.filter(subjects__exam=exam)\
                        .update(exam=exam)

    # Delete orphan questions
    Question.objects.filter(subjects__isnull=True).delete()

def remove_exams(apps, schema_editor):
    Question = apps.get_model('exams', 'Question')
    Question.objects.update(exam=None)

class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0036_question_exam'),
    ]

    operations = [
        migrations.RunPython(add_exams,
                             reverse_code=remove_exams)
    ]
