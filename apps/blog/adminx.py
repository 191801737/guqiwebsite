#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xadmin

from .models import Article


class ArticleAdmin(object):
    list_display = ['title', 'author', 'pub_date', 'update_time']
    list_filter = ['title', 'author', 'pub_date', 'update_time']
    search_fields = ['title', 'author']


xadmin.site.register(Article, ArticleAdmin)
