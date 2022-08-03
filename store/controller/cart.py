from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from store.models import Cart,Product
from django.contrib.auth.decorators import login_required

def addToCart(request):
    if request.method == 'POST':
        if request.user.is_authenticated:
            prod_id = int(request.POST.get('product_id'))
            product_check = Product.objects.get(id = prod_id)
            if product_check:
                if Cart.objects.filter(user_id = request.user.id, product_id = prod_id):
                    return JsonResponse({'status': 'Product Already in Cart'})
                else:
                    prod_qty = int(request.POST.get('product_qty'))
                    
                    if product_check.quantity >= prod_qty:
                        Cart.objects.create(user = request.user,
                                            product_id = prod_id,
                                            product_qty = prod_qty)
                        return JsonResponse({'status': 'Product Added successfully'})
                    else:
                        return JsonResponse({'status': 'Only' + str(product_check.quantity) + 'quantity available'})
            else:
                return JsonResponse({'status': 'No such product found'})
        else:
            return JsonResponse({'status': 'Login to continue'})
    return redirect('/')

@login_required()
def cartView(request):
    cart = Cart.objects.filter(user=request.user)
    context = {'cart': cart}
    return render(request, 'store/cart.html', context)

def updateCart(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        if Cart.objects.filter(user_id = request.user.id, product_id = prod_id):
            prod_qty = int(request.POST.get('product_qty'))
            cart = Cart.objects.get(user = request.user,
                                    product_id = prod_id)
            cart.product_qty = prod_qty
            cart.save()
            return JsonResponse({'status': 'Updated Successfully'})
    return redirect('/')

def deleteItemCart(request, itemCart_id):
    item = Cart.objects.get(id = itemCart_id, user_id = request.user)
    item.delete()
    messages.warning(request, 'Product Deleted')
    
    return redirect('CartView')