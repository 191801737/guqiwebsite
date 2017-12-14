#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xadmin

from .models import Article, Case, Introduce, IntroduceBanner, NewsBanner


class IntroduceBannerAdmin(object):
    list_display = ['image', 'url', 'add_time']
    list_filter = ['image', 'url', 'add_time']
    search_fields = ['image', 'url']


class NewsBannerAdmin(object):
    list_display = ['image', 'url', 'add_time']
    list_filter = ['image', 'url', 'add_time']
    search_fields = ['image', 'url']


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


xadmin.site.register(IntroduceBanner, IntroduceBannerAdmin)
xadmin.site.register(NewsBanner, NewsBannerAdmin)
xadmin.site.register(Article, ArticleAdmin)
xadmin.site.register(Case, CaseAdmin)
xadmin.site.register(Introduce, IntroduceAdmin)
