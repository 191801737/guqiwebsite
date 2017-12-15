# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-15 13:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20171215_1321'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='商品分类')),
                ('desc', models.CharField(blank=True, default='', max_length=300, null=True, verbose_name='商品描述')),
                ('image', models.ImageField(blank=True, default='image/default.png', null=True, upload_to='product/%Y/%m', verbose_name='商品封面图')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('style', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Style', verbose_name='样式')),
            ],
            options={
                'verbose_name_plural': '商品分类',
                'verbose_name': '商品分类',
            },
        ),
    ]
