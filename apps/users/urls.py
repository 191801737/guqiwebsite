#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url


from .views import index,about


urlpatterns = [
    # 文章列表
    url(r'^about/$', about, name='about'),




]
