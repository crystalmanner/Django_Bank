# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-18 07:22
from __future__ import unicode_literals

from django.db import migrations

def set_has_finished(apps, schema_editor):
    Session = apps.get_model('exams', 'Session')

    for session in Session.objects.exclude(session_mode__in=['INCOMPLETE', 'SOLVED']):
        if session.questions.filter(is_deleted=False)\
                            .exclude(answer__session=session)\
                            .distinct().exists():
            session.has_finished = False
            print("{} has not finished".format(session.pk))
        else:
            session.has_finished = True
            print("{} has finished".format(session.pk))
        session.save()

def unset_has_finished(apps, schema_editor):
    Session = apps.get_model('exams', 'Session')
    Session.objects.update(has_finished=None)

class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0059_session_has_finished'),
    ]

    operations = [
        migrations.RunPython(set_has_finished,
                             reverse_code=unset_has_finished)
    ]
