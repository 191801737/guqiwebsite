# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-20 21:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20171120_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='image/%Y/%m', verbose_name='头像'),
        ),
    ]
