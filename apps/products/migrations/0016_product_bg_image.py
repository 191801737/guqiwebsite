# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-21 23:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0015_auto_20171215_2313'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='bg_image',
            field=models.ImageField(blank=True, default='image/default.png', null=True, upload_to='product/%Y/%m', verbose_name='样式背景图'),
        ),
    ]
