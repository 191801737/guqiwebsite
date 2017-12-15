from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, render_to_response, HttpResponse
from .models import Product, Style, Category


# Create your views here.


class ProductListView(View):
    """
    产品列表页
    """

    def get(self, request):

        # 获取所有产品
        all_products = Product.objects.all()

        # 对产品进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_products, 6, request=request)

        products = p.page(page)

        return render(request, 'products.html', locals())


class ProductStyleView(View):
    """
    产品样式页
    """
    def get(self, request, product_id):

        # 获取产品对应的样式
        product = Product.objects.get(id=int(product_id))

        all_styles = product.get_product_style()
        # 对样式进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_styles, 6, request=request)

        styles = p.page(page)

        return render(request, "product-style.html", locals())


class ProductCategoryView(View):
    """商品分类"""

    def get(self, request, style_id):
        style = Style.objects.get(id=int(style_id))

        return render(request, 'product-list.html', locals())


class ProductPictureView(View):
    """商品图片"""

    def get(self, request, category_id):
        category = Category.objects.get(id=int(category_id))

        return render(request, 'produce-detail.html', locals())
