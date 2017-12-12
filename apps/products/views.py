from django.shortcuts import render
from django.views.generic import View
from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, render_to_response, HttpResponse
from .models import Product, Picture


# Create your views here.


class ProductListView(View):
    """
    产品列表页
    """

    def get(self, request):

        all_products = Product.objects.all()

        return render(request, 'products.html', locals())


class ProductStyleView(View):
    """
    产品风格页
    """
    def get(self, request, product_id):
        product = Product.objects.get(id=int(product_id))

        return render(request, "produce-style.html", locals())

def productStyle(request):
    return render_to_response('product-style.html', locals())
