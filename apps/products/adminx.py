#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xadmin

from .models import Product, Style, Picture, ProductStyleBanner, ProductPictureBanner


class ProductStyleBannerAdmin(object):
    list_display = ['image', 'url', 'add_time']
    list_filter = ['image', 'url', 'add_time']
    search_fields = ['image', 'url']


class ProductPictureBannerAdmin(object):
    list_display = ['image', 'url', 'add_time']
    list_filter = ['image', 'url', 'add_time']
    search_fields = ['image', 'url']


class ProductAdmin(object):
    list_display = ['name', 'desc', 'image', 'add_time']
    list_filter = ['name', 'desc', 'image', 'add_time']
    search_fields = ['name', 'desc']


class StyleAdmin(object):
    list_display = ['product', 'name', 'desc', 'image', 'add_time']
    list_filter = ['product__name', 'name', 'desc', 'image', 'add_time']
    search_fields = ['product__name', 'name', 'image', 'desc']


# class CategoryAdmin(object):
#     list_display = ['style', 'name', 'desc', 'image', 'add_time']
#     list_filter = ['style__name', 'name', 'desc', 'image', 'add_time']
#     search_fields = ['style__name', 'name', 'image', 'desc']


class PictureAdmin(object):
    list_display = ['category', 'name', 'image', 'add_time']
    list_filter = ['category__name', 'name', 'image', 'add_time']
    search_fields = ['category__name', 'image', 'name']


xadmin.site.register(Product, ProductAdmin)
xadmin.site.register(Style, StyleAdmin)
# xadmin.site.register(Category, CategoryAdmin)
xadmin.site.register(Picture, PictureAdmin)
xadmin.site.register(ProductStyleBanner, ProductStyleBannerAdmin)
xadmin.site.register(ProductPictureBanner, ProductPictureBannerAdmin)



