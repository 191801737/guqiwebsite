# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 09:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20171126_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='image/default.png', upload_to='blog/%Y/%m', verbose_name='封面图'),
        ),
    ]
