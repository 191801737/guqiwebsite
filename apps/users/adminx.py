#!/usr/bin/env python
# -*- coding: utf-8 -*-


import xadmin
from xadmin import views

from .models import IndexBanner, ProductBanner, CaseBanner


# 设置主题
class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '后台管理系统'
    site_footer = '后台管理系统'
    menu_style = 'accordion'


class IndexBannerAdmin(object):
    list_display = ['image', 'url', 'add_time']
    list_filter = ['image', 'url', 'add_time']
    search_fields = ['image', 'url']


class ProductBannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']


class CaseBannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']


xadmin.site.register(IndexBanner, IndexBannerAdmin)
xadmin.site.register(ProductBanner, ProductBannerAdmin)
xadmin.site.register(CaseBanner, CaseBannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
