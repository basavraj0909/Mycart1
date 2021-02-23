from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

def index(request):
    products = Product.objects.all()
    print(products)
    n = len(products)
    nslides = n//4 + ceil((n/4)-(n//4))
    params = {'no_of_slides' :nslides, 'range':range(1,nslides), 'product': products}
    return render(request, 'shop/index.html', params)
    # products = Product.objects.all()
    # print(products)
'''
    allprods = []
    catprods = Product.objects.values('category','id')
    cats =  {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nslides = n // 4 + ceil((n / 4) - (n // 4))
        allprods.append([prod,range(1,nslides),nslides])

    #
    # allprods =[[products,range(1,nslides),nslides],
    #            [products,range(1,nslides),nslides]]
    params = {'allprods' : allprods}
    '''

def about(request):
    return render(request, 'shop/about .html')


def contact(request):
    return HttpResponse("you are at contact")


def tracker(request):
    return HttpResponse("you are at tracker")


def search(request):
    return HttpResponse("you are at search")

def productView(request):
    return HttpResponse("you are at productView")

def checkout(request):
    return HttpResponse("you are at checkout")
#     path('/', views.prodView, name='ProductView'),

