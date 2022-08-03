import re
from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from store.models import Order, OrderItem
from django.contrib.auth.decorators import login_required

def myOrders(request):
    orders = Order.objects.filter(user = request.user)
    context = {'orders': orders}
    return render(request, 'store/order/orders.html', context)

def orderDetail(request, tracking_nro):
    order = Order.objects.get(tracking_no = tracking_nro, user = request.user)
    order_items = OrderItem.objects.filter(order = order)
    context = {'order': order, 'order_items': order_items}
    return render(request, 'store/order/orderDetail.html', context)
