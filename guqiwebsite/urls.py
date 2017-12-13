"""guqiwebsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.views.static import serve


from apps.users import views as users_views
import xadmin

from guqiwebsite.settings import MEDIA_ROOT
from users.views import IndexView
from products import views as product_views

urlpatterns = [
    # 管理界面的url
    url(r'^admin/', xadmin.site.urls),

    # 首页的URL
    url(r'^$', IndexView.as_view(), name='index'),

    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)/$', serve, {'document_root': MEDIA_ROOT}),

    # 课程机构url
    url(r'^blog/', include('blog.urls', namespace='blog'), ),

    # 用户界面的url
    url(r'^users/', include('users.urls', namespace='users'), ),

    # 产品界面的url
    url(r'^product/', include('products.urls', namespace='products'), ),

    # 富文本相关url
    url(r'^ueditor/', include('DjangoUeditor.urls')),
    url(r'^productstyle/', product_views.productStyle, name='productStyle'),
    url(r'^productlist/', product_views.productList, name='productList'),
    url(r'^productdetail/', product_views.productDetail, name='productDetail'),
]

# 全局XXX页面配置
handler403 = 'users.views.page_forbidden'
handler404 = 'users.views.page_not_foud'
handler500 = 'users.views.page_error'
