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