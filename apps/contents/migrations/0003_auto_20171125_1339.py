# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contents', '0002_auto_20171125_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='tag',
            field=models.CharField(blank=True, default='', max_length=10, null=True, verbose_name='产品标签'),
        ),
    ]