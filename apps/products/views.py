from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import Product, Style,  ProductStyleBanner, ProductPictureBanner


# Create your views here.


class ProductListView(View):
    """
    产品列表页
    """

    def get(self, request):

        # 获取所有产品
        products = Product.objects.all()

        return render(request, 'products.html', locals())


class ProductStyleView(View):
    """
    产品样式页
    """
    def get(self, request, product_id):

        # 获取背景图
        productstylebanners = ProductStyleBanner.objects.all()[:1]

        # 获取所有产品
        all_products = Product.objects.all()

        # 获取产品对应的样式
        product = Product.objects.get(id=int(product_id))

        # 获取产品所有风格
        all_styles = product.get_product_style()

        # 对样式进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_styles, 9, request=request)

        styles = p.page(page)

        return render(request, "product-style.html", locals())


# class ProductCategoryView(View):
#     """商品分类"""
#
#     def get(self, request, style_id):
#         style = Style.objects.get(id=int(style_id))
#
#         all_categorys = style.get_style_category()
#
#         # 对商品类别进行分页
#         try:
#             page = request.GET.get('page', 1)
#         except PageNotAnInteger:
#             page = 1
#
#         # Provide Paginator with the request object for complete querystring generation
#
#         p = Paginator(all_categorys, 9, request=request)
#
#         categorys = p.page(page)
#
#         return render(request, 'product-list.html', locals())


class ProductPictureView(View):
    """商品图片"""

    def get(self, request, style_id):

        # 获取背景图
        productpicturebanners = ProductPictureBanner.objects.all()[:1]

        style = Style.objects.get(id=int(style_id))

        # 获取风格所有的图片
        all_pictures = style.get_style_picture()

        # 对商品类别进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        # Provide Paginator with the request object for complete querystring generation

        p = Paginator(all_pictures, 9, request=request)

        pictures = p.page(page)

        return render(request, 'product-list.html', locals())
