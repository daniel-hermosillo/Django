# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-06 00:45
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quizapplication',
            name='answer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='quiz.Answer'),
        ),
    ]
