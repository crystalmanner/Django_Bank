# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-13 17:17
from __future__ import unicode_literals

from django.db import migrations

def add_categories(apps, schema_editor):
    Category = apps.get_model('exams', 'Category')
    Exam = apps.get_model('exams', 'Exam')
    Subject = apps.get_model('exams', 'Subject')

    ksau_hs = Category.objects.create(name="KSAU-HS", slug='ksau-hs')
    com = Category.objects.create(name="College of Medicine",
                                  slug='com', parent_category=ksau_hs)
    basic = Category.objects.create(name="Basic years", slug='basic',
                                    parent_category=com)
    clinical = Category.objects.create(name="Clinical years",
                                       slug='clinical',
                                       parent_category=com)
    basic_subjects = ['Anatomy', 'Biochemistry and Immunology',
                      'Clinical', 'EBM', 'Histology', 'Pathology',
                      'Physiology']

    exam_map = {'Foundation': basic_subjects,
                'MSK': basic_subjects,
                'Respiratory': basic_subjects,
                'Hematology':  basic_subjects,
                'Cardiology': basic_subjects,
                'Neurology':  basic_subjects,
                'Endocrinology': basic_subjects,
                'GIT': basic_subjects,
                'Urology': basic_subjects,
                'Oncology': basic_subjects,
                'Medicine I': ['Emergency medicine', 'Endocrinology',
                                  'Gastroenterology & hepatology',
                                  'Infectious diseases',
                                  'Nephrology & urinary disorders',
                                  'Respiratory medicine',
                                  'Rheumatology',
                                  'General medicine/Others'],
                'Pediatric': ['Developmental & behavior clinical pediatrics',
                                 'Endocrinology', 'Genetics and Dysmorphology',
                                 'Hematology/oncology',
                                 'Neonatology', 'Neurology',
                                 'Pediatric cardiology',
                                 'Pediatric infectious disease',
                                 'General Pediatrics/Others'],
                'Surgery I': ['Appendix', 'Breast', 'Gallbladder',
                                 'Genitururinary track', 'Hernias', 'Lower GI',
                                 'Pancreas', 'Pediatrics', 'Thyroid',
                                 'Trauma & emergency ', 'Upper GI',
                                 'Vascualr', 'Others'],
                'Family Medicine': ['Community medicine & communication',
                                       'General medicine ',
                                       'Pediatrics', 'Psychiatry',
                                       'Women\'s health'],
                'Medicine II': ['Cardiovascular Disease', 'Hematology',
                                   'Medical Oncology', 'General Medicine/Others'],
                'Surgery II': ['Anesthesia', 'Orthopedics',
                                  'Plastic Surgery', 'Others'],
                'Obstetrics & Gynecology': ['Obstetrics', 'Gynecology'],
                'Special Senses and Mental Health': ['Neurology', 'Ophthalmology', 'Otolaryngology', 'Psychiatry']
    }

    for exam in exam_map:
        subjects = exam_map[exam]
        if subjects == basic_subjects:
            category = basic
        else:
            category = clinical

        exam = Exam.objects.create(name=exam,
                                    category=category)

        for subject_name in subjects:
            Subject.objects.create(name=subject_name, exam=exam)

class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(add_categories)
    ]
                   
