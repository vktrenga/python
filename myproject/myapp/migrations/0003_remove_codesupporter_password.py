# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 17:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_codesupporter_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codesupporter',
            name='password',
        ),
    ]
