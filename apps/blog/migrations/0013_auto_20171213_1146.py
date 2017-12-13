# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 11:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20171213_1118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='introduce',
            name='content',
            field=models.TextField(default='', verbose_name='公司简介'),
        ),
        migrations.AlterField(
            model_name='introduce',
            name='culture',
            field=models.TextField(default='', verbose_name='企业文化'),
        ),
        migrations.AlterField(
            model_name='introduce',
            name='idea',
            field=models.TextField(default='', verbose_name='经营理念'),
        ),
    ]
