# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-24 10:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_registor_user_user_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='registor_user',
            name='contact_no',
            field=models.CharField(default='', max_length=20),
        ),
    ]
