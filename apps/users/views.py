from django.shortcuts import render
from django.shortcuts import render, render_to_response, HttpResponse
# Create your views here.


def index(request):
    return render_to_response('index.html', locals())


def about(request):
    return render_to_response('CompanyProfile.html', locals())


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

