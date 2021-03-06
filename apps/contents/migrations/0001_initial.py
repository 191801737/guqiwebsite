# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 13:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='产品名称')),
                ('desc', models.CharField(max_length=300, verbose_name='产品描述')),
                ('detail', models.TextField(verbose_name='产品详情')),
                ('is_banner', models.BooleanField(default=False, verbose_name='是否轮播')),
                ('image', models.ImageField(upload_to='courses/%Y/%m', verbose_name='封面图片')),
                ('tag', models.CharField(default='', max_length=10, verbose_name='产品标签')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
            ],
        ),
    ]
