# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 13:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0004_auto_20171125_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='is_banner',
        ),
    ]
