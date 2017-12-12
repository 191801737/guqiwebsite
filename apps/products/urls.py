#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url


from .views import ProductListView, ProductStyleView


urlpatterns = [
    # 产品列表
    url(r'^list/$', ProductListView.as_view(), name='product_list'),

    #产品样式
    # url(r'^style/$', ProductListView.as_view(), name='product_style'),

    # 产品详情页
    url(r'^detail/(?P<product_id>\d+)$', ProductStyleView.as_view(), name='product_detail'),


]
