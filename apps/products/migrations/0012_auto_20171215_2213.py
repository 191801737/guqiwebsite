# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-15 22:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_remove_product_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='style',
        ),
        migrations.RemoveField(
            model_name='picture',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Picture',
        ),
    ]
