# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-13 20:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_auto_20171213_1149'),
    ]

    operations = [
        migrations.AddField(
            model_name='case',
            name='desc',
            field=models.CharField(default='', max_length=256, verbose_name='描述'),
        ),
    ]
