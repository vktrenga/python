# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2011-01-01 00:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_auto_20110101_0004'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Codesupporter',
        ),
        migrations.DeleteModel(
            name='User_Registor',
        ),
    ]
