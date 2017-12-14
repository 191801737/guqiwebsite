#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import  products, SuccessProducts

from .views import IndexView

urlpatterns = [
    # 文章列表
    # url(r'^about/$', about, name='about'),
    # url(r'^news/$', news, name='news'),
    url(r'^products/$', products, name='products'),
    url(r'^SuccessProducts/$', SuccessProducts, name='SuccessProducts'),


]
