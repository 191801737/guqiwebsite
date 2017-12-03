#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url


from .views import ArticleView, ArticleDetailView


urlpatterns = [
    # 文章列表
    url(r'^list/$', ArticleView.as_view(), name='articles_list'),

    # 文章详情页
    url(r'^detail/(?P<article_id>\d+)/$', ArticleDetailView.as_view(), name='article_detail'),

    # 成功案例列表
    url(r'^story_list/$', ArticleView.as_view(), name='story_list'),

    # 成功案例详情页
    url(r'^story_detail/(?P<article_id>\d+)/$', ArticleDetailView.as_view(), name='story_detail'),

]
