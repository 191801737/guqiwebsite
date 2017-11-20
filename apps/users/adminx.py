#!/usr/bin/env python
# -*- coding: utf-8 -*-


import xadmin
from xadmin import views

from .models import Banner


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']


xadmin.site.register(Banner, BannerAdmin)