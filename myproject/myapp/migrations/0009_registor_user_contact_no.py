# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-23 02:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_auto_20160723_0123'),
    ]

    operations = [
        migrations.AddField(
            model_name='registor_user',
            name='contact_no',
            field=models.CharField(default="test", max_length=20),
            preserve_default=False,
        ),
    ]
