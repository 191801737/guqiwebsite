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
        all_articles = Article.objects.all()

        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_articles, 3, request=request)

        articles = p.page(page)

        return render(request, 'blog-list.html', locals())


class ArticleDetailView(View):
    """
    文章详情
    """

    def get(self, request, article_id):
        article = Article.objects.get(id=int(article_id))
        return render(request, 'blog-detail.html', locals())
