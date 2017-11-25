from django.shortcuts import render

# Create your views here.


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
