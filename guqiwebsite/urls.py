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


urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^admin/', xadmin.site.urls),

    url(r'^$|^index/$', users_views.index, name='index'),  # 首页
    url(r'^about/$', users_views.about, name='about'),  # 关于我们
    url(r'^news/$', users_views.news, name='news'),  # 新闻
    url(r'^products/$', users_views.products, name='products'),  # 产品
    url(r'^SuccessProducts/$', users_views.SuccessProducts, name='SuccessProducts'),  # 案例

    # 配置上传文件的访问处理函数
    url(r'^media/(?P<path>.*)/$', serve, {'document_root': MEDIA_ROOT}),


    # 课程机构url
    url(r'^blog/', include('blog.urls', namespace='blog'), ),

    # 用户界面的url
    url(r'^users/', include('users.urls', namespace='users'), ),

    # 产品界面的url
    url(r'^product/', include('products.urls', namespace='products'), ),

]

# 全局XXX页面配置
handler403 = 'user.views.page_forbidden'
handler404 = 'user.views.page_not_foud'
handler500 = 'user.views.page_error'
