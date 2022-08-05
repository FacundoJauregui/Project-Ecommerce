from hashlib import new
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from store.models import Cart, Order, OrderItem, Product, Profile
from django.contrib.auth.decorators import login_required
import random


def checkoutView(request):
    cartitems = Cart.objects.filter(user = request.user)
    total_price = 0
    for item in cartitems:
        if item.product_qty > item.product.quantity:
            Cart.objects.get(id = item.id).delete()
        else:
            total_price += item.product.selling_price * item.product_qty
            
    user_profile = Profile.objects.filter(user = request.user).first()
              
    context = {'cartitems': cartitems, 'total_price':total_price,'user_profile': user_profile}
    return render(request, 'store/checkout.html', context)

def placeOrder(request):
    

    if request.method == 'POST':
        current_user = request.user
        
        if not Profile.objects.filter(user = request.user):
            profile = Profile()
            profile.user = current_user
            profile.phone = request.POST.get('phone')
            profile.address = request.POST.get('address')
            profile.country = request.POST.get('country')
            profile.state = request.POST.get('state')
            profile.city = request.POST.get('city')
            profile.pin_code = request.POST.get('pincode')
            profile.save()
        
        
        neworder = Order()
        neworder.user = request.user
        neworder.fname = request.POST.get('fname')
        neworder.lname = request.POST.get('lname')
        neworder.email = request.POST.get('email')
        neworder.phone = request.POST.get('phone')
        neworder.address = request.POST.get('address')
        neworder.country = request.POST.get('country')
        neworder.state = request.POST.get('state')
        neworder.city = request.POST.get('city')
        neworder.pin_code = request.POST.get('pincode')
        
        neworder.payment_method = request.POST.get('payment_method')
        
        cart = Cart.objects.filter(user = request.user)
        cart_total_price = 0
        for item in cart:
            cart_total_price += item.product.selling_price * item.product_qty
        
        neworder.total_price = cart_total_price
        
        trackno = 'fej' + str(random.randint(1111111,9999999))
        while Order.objects.filter(tracking_no = trackno) is None:
            trackno = 'fej' + str(random.randint(1111111,9999999))
            
        neworder.tracking_no = trackno
        neworder.save()
        
        neworderitems = Cart.objects.filter(user = request.user)
        for item in neworderitems:
            OrderItem.objects.create(
                order = neworder,
                product = item.product,
                price = item.product.selling_price,
                quantity = item.product_qty,
            )
            
            #To decrease the product quantity from available stock
            order_product = Product.objects.get(id = item.product_id)
            order_product.quantity -= item.product_qty
            order_product.save()
        
        #To clear user's cart
        Cart.objects.filter(user = request.user).delete()
        
        pay_method = request.POST.get('payment_method')
        if pay_method == 'Paid with PayPal':
            return JsonResponse({'status': 'Your order has been placed successfully'})
        else:
            messages.success(request, 'Your order has been placed succesfully')
                              
    return redirect('Home')


    