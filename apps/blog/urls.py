#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url


from .views import ArticleView, ArticleDetailView, IntroduceView, CaseView, CaseDetailView


urlpatterns = [
    # 新闻列表
    url(r'^news_list/$', ArticleView.as_view(), name='news_list'),

    # 新闻详情页
    url(r'^news_detail/(?P<article_id>\d+)/$', ArticleDetailView.as_view(), name='news_detail'),

    # 成功案例列表
    url(r'^story_list/$', CaseView.as_view(), name='story_list'),

    # 成功案例详情页
    url(r'^story_detail/(?P<case_id>\d+)/$', CaseDetailView.as_view(), name='story_detail'),

    # 关于我们
    url(r'^introduce/$', IntroduceView.as_view(), name='Introduce'),

]
