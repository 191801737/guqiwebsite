#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url


from .views import ProductListView, ProductStyleView, ProductCategoryView, ProductPictureView

urlpatterns = [
    # 产品列表
    url(r'^list/$', ProductListView.as_view(), name='product_list'),

    # 产品样式
    url(r'^style/(?P<product_id>\d+)/$', ProductStyleView.as_view(), name='product_style'),

    # 商品分类
    url(r'^category/(?P<style_id>\d+)/$', ProductCategoryView.as_view(), name='product_category'),

    # 商品图片
    url(r'^picture/(?P<category_id>\d+)$', ProductPictureView.as_view(), name='product_picture'),

]
