from cgi import print_directory
import re
from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *
from django.http import JsonResponse
    
def home(request):
    if request.GET:
        product_search = request.GET['productsearch']
        products = Product.objects.filter(name__icontains = product_search)
        context = {'products': products}
        return render(request, 'store/products/productSearchList.html', context)
    
    trending_products = Product.objects.filter(trending = 1)[:10]
    aux = Product.objects.filter(tag = 'Hot')
    hot_products = aux.filter(trending = 0)
    
    context = {'trending_products': trending_products, 'hot_products': hot_products}
      
    return render(request,'store/index.html', context)

def categorys(request):
    category = Category.objects.filter(status = 0)
    context = {'category': category}
    return render(request, 'store/collections.html', context)


def categorysview(request, slug):   
    if Category.objects.filter(slug = slug, status = 0):
        products= Product.objects.filter(category__slug = slug)
        category= Category.objects.get(slug = slug)
        context = {'products': products, 'category': category}
        print(slug)
        return render(request, 'store/products/index.html',context)
    else:
        messages.warning(request, "No se encuentra tal categoria")
        return redirect('CategorysView')

def productview(request,cat_slug, prod_slug):
    if Category.objects.filter(slug = cat_slug, status = 0):
        if Product.objects.filter(slug = prod_slug, status = 0):
            product = Product.objects.get(slug = prod_slug, status = 0)
            context = {'product': product}
        else:
            messages.error(request, "No se encuentra tal producto")
            return redirect('CategorysView')
    else:
        messages.error(request, "No se encuentra tal categoria")
        return redirect('CategorysView')
    
    return render(request, 'store/products/productView.html', context)

def productListAjax(request):
    products = Product.objects.filter(status=0).values_list('name', flat=True)
    product_list = list(products)
    
    return JsonResponse(product_list, safe=False)
