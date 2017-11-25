#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xadmin

from .models import Product


class ProductAdmin(object):
    list_display = ['name', 'desc', 'tag', 'image', 'add_time']
    list_filter = ['name', 'desc', 'tag', 'image', 'add_time']
    search_fields = ['name', 'desc', 'tag']


xadmin.site.register(Product, ProductAdmin)
