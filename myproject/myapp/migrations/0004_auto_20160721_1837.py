# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-21 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_remove_codesupporter_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=50)),
                ('passwordnew', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'codesupporter_user',
            },
        ),
        migrations.AddField(
            model_name='codesupporter',
            name='passwordnew',
            field=models.CharField(default=1, max_length=40),
            preserve_default=False,
        ),
    ]
