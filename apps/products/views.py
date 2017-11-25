from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger

from .models import Product


# Create your views here.


class ProductListView(View):
    """
    产品列表页
    """

    def get(self, request):

        all_products = Product.objects.all().order_by('-add_time')

        # 对课程进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_products, 3, request=request)

        products = p.page(page)

        return render(request, 'produce-list.html', locals())


class CourseDetailView(View):
    """
    产品详情页
    """
    def get(self, request, product_id):
        product = Product.objects.get(id=int(product_id))

        return render(request, "produce-detail.html", locals())
