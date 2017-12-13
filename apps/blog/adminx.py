#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xadmin

from .models import Article, Case, Introduce


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


class IntroduceAdmin(object):
    list_display = ['title', 'pub_date', 'update_time']
    list_filter = ['title', 'pub_date', 'update_time']
    style_fields = {"content": "ueditor", "culture": "ueditor", "idea": "ueditor", "contact": "ueditor"}


xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Case, CaseAdmin)
xadmin.site.register(Introduce, IntroduceAdmin)
