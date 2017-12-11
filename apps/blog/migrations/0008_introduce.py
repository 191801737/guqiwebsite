# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-03 16:15
from __future__ import unicode_literals

import DjangoUeditor.models
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20171203_1219'),
    ]

    operations = [
        migrations.CreateModel(
            name='Introduce',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='标题')),
                ('content', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('image', models.ImageField(blank=True, default='image/default.png', null=True, upload_to='blog/%Y/%m', verbose_name='封面图')),
                ('author', models.CharField(default='管理员', max_length=100, verbose_name='作者')),
                ('pub_date', models.DateTimeField(default=datetime.datetime.now, verbose_name='发表时间')),
                ('update_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='更新时间')),
            ],
            options={
                'verbose_name': '关于我们',
                'verbose_name_plural': '关于我们',
            },
        ),
    ]