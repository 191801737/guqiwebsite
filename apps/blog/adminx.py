#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xadmin

from .models import Article, Case


class ArticleAdmin(object):
    list_display = ['title', 'author', 'pub_date', 'update_time']
    list_filter = ['title', 'author', 'pub_date', 'update_time']
    search_fields = ['title', 'author']
    style_fields = {"content": "ueditor"}


class CaseAdmin(object):
    list_display = ['title', 'author', 'pub_date', 'update_time']
    list_filter = ['title', 'author', 'pub_date', 'update_time']
    search_fields = ['title', 'author']
    style_fields = {"content": "ueditor"}


xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Case, CaseAdmin)
