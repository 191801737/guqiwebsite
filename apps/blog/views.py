from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import View

# Create your views here.
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Article


class ArticleView(View):
    """
    文章列表
    """

    def get(self, request):
        # 获取文章所有内容
        articles = Article.objects.all()
        return render(request, 'blog-list.html', locals())


class ArticleDetailView(View):
    """
    文章详情
    """

    def get(self, request, article_id):
        article = Article.objects.get(id=int(article_id))
        return render(request, 'blog-detail.html', locals())
