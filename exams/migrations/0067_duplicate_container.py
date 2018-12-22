# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-03-03 13:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('exams', '0066_duplicate'),
    ]

    operations = [
        migrations.CreateModel(
            name='DuplicateContainer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('revision_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('PENDING', 'Pending'), ('KEPT', 'Kept'), ('DECLINED', 'Declined')], default='PENDING', max_length=20)),
                ('submission_date', models.DateTimeField(auto_now_add=True)),
                ('primary_question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary_duplicates', to='exams.Question')),
                ('reviser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='duplicate',
            name='question',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='secondary_duplicates', to='exams.Question'),
        ),
        migrations.AddField(
            model_name='duplicate',
            name='container',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='exams.DuplicateContainer'),
        ),
    ]
