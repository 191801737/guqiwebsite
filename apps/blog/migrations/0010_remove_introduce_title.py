# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 16:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20171203_1620'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='introduce',
            name='title',
        ),
    ]