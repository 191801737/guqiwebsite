#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url


from .views import ProductListView, CourseDetailView


urlpatterns = [
    # 产品列表
    url(r'^list/$', ProductListView.as_view(), name='product_list'),

    # 产品详情页
    url(r'^detail/(?P<product_id>\d+)$', CourseDetailView.as_view(), name='product_detail'),


]
