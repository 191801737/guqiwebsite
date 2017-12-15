#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xadmin

from .models import Product, Style, Category, Picture


class ProductAdmin(object):
    list_display = ['name', 'desc', 'tag', 'image', 'add_time']
    list_filter = ['name', 'desc', 'tag', 'image', 'add_time']
    search_fields = ['name', 'desc', 'tag']


class StyleAdmin(object):
    list_display = ['product', 'name', 'desc', 'add_time']
    list_filter = ['product__name', 'name', 'desc', 'add_time']
    search_fields = ['product__name', 'name', 'desc']


class CategoryAdmin(object):
    list_display = ['style', 'name', 'desc', 'add_time']
    list_filter = ['style__name', 'name', 'desc', 'add_time']
    search_fields = ['style__name', 'name', 'desc']


class PictureAdmin(object):
    list_display = ['category', 'name', 'add_time']
    list_filter = ['category__name', 'name', 'add_time']
    search_fields = ['category__name', 'name']


xadmin.site.register(Product, ProductAdmin)
xadmin.site.register(Style, StyleAdmin)
xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Picture, PictureAdmin)



