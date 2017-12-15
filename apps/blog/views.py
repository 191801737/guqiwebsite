from django.shortcuts import render
from django.shortcuts import render
from django.views.generic import View

# Create your views here.
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Article, Case, Introduce, IntroduceBanner, NewsBanner


class ArticleView(View):
    """
    新闻列表
    """

    def get(self, request):

        # 获取新闻中心的背景图
        newsbanners = NewsBanner.objects.all()[:1]

        # 获取新闻所有内容
        all_articles = Article.objects.all()

        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_articles, 8, request=request)

        articles = p.page(page)

        return render(request, 'news.html', locals())


class ArticleDetailView(View):
    """
    新闻详情
    """

    def get(self, request, article_id):
        article = Article.objects.get(id=int(article_id))
        return render(request, 'blog-detail.html', locals())


class CaseView(View):
    """
    成功案例列表
    """

    def get(self, request):
        # 获取成功案例所有内容
        all_cases = Case.objects.all()

        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_cases, 8, request=request)

        cases = p.page(page)

        return render(request, 'SuccessProducts.html', locals())


class CaseDetailView(View):
    """
    成功案例详情
    """

    def get(self, request, case_id):
        article = Case.objects.get(id=int(case_id))
        return render(request, 'SuccessProductsDetail.html', locals())


class IntroduceView(View):
    """关于我们"""

    def get(self, request):

        # 关于我们的背景图
        introducebanners = IntroduceBanner.objects.all()[:1]

        # 关于我们的内容
        introduces = Introduce.objects.all()

        return render(request, 'CompanyProfile.html', locals())
