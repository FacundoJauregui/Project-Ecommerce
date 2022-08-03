from django.shortcuts import redirect, render
from django.contrib import messages
from .models import *

def home(request):
    return render(request,'store/index.html')

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