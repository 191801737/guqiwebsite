# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 13:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='image',
            field=models.ImageField(default='image/default.png', upload_to='blog/%Y/%m', verbose_name='文章图片'),
        ),
    ]
