from django.shortcuts import render
from django.shortcuts import render, render_to_response, HttpResponse
from django.views.generic.base import View
from .models import IndexBanner, ProductBanner, CaseBanner


# Create your views here.

class IndexView(View):
    """guqiwebsite的首页"""

    def get(self, request):
        # 首页背景图
        indexbanners = IndexBanner.objects.all()[:1]

        # 产品轮播图
        productbanners = ProductBanner.objects.all()[:3]

        # 成功案例轮播图
        casebanners = CaseBanner.objects.all()[:3]
        return render(request, 'index.html', locals())


def news(request):
    return render_to_response('news.html', locals())


def products(request):
    return render_to_response('products.html', locals())


def SuccessProducts(request):
    return render_to_response('SuccessProducts.html', locals())


def page_forbidden(request):
    # 全局403处理函数
    response = render(request, '403.html', locals())
    response.status_code = 403
    return response


def page_not_foud(request):
    # 全局404处理函数
    response = render(request, '404.html', locals())
    response.status_code = 404
    return response


def page_error(request):
    # 全局500处理函数
    response = render(request, '500.html', locals())
    response.status_code = 500
    return response
