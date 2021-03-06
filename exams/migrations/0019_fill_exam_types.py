# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-04 09:50
from __future__ import unicode_literals

from django.db import migrations


exam_type_choices = (
    ('FINAL', 'Final'),
    ('MIDTERM', 'Midterm'),
    ('FORMATIVE', 'Formative'),
    ('OSPE','OSPE'),
)

def add_exam_types(apps, schema_editor):
    Session = apps.get_model('exams', 'Session')
    Question = apps.get_model('exams', 'Question')
    ExamType = apps.get_model('exams', 'ExamType')
    Category = apps.get_model('exams', 'Category')

    ksau_hs = Category.objects.get(slug='ksau-hs')
    for code_name, human_name in exam_type_choices:
        exam_type = ExamType.objects.create(name=human_name,
                                            code_name=code_name,
                                            category=ksau_hs)
        exam_type.question_set.add(*Question.objects.filter(exam_type=code_name))
        exam_type.session_set.add(*Session.objects.filter(session_type=code_name))

def remove_exam_types(apps, schema_editor):
    Session = apps.get_model('exams', 'Session')
    Question = apps.get_model('exams', 'Question')
    ExamType = apps.get_model('exams', 'ExamType')

    for code_name, human_name in exam_type_choices:
        exam_type = ExamType.objects.get(code_name=code_name)
        questions = Question.objects.filter(exam_types=exam_type)\
                                    .update(exam_type=code_name, exam_types=None)
        #exam_type.question_set.remove(*questions)
        exam_type.delete()


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0018_add_exam_types'),
    ]

    operations = [
        migrations.RunPython(add_exam_types,
                             reverse_code=remove_exam_types)

    ]
