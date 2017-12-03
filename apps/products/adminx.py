#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xadmin

from .models import Product, Style, Picture


class ProductAdmin(object):
    list_display = ['name', 'desc', 'tag', 'image', 'add_time']
    list_filter = ['name', 'desc', 'tag', 'image', 'add_time']
    search_fields = ['name', 'desc', 'tag']


class StyleAdmin(object):
    list_display = ['product', 'name', 'add_time']
    list_filter = ['product__name', 'name', 'add_time']
    search_fields = ['product__name', 'name']


class PictureAdmin(object):
    list_display = ['style', 'name', 'add_time']
    list_filter = ['style__name', 'name', 'add_time']
    search_fields = ['style__name', 'name']


xadmin.site.register(Product, ProductAdmin)
xadmin.site.register(Style, StyleAdmin)
xadmin.site.register(Picture, PictureAdmin)



