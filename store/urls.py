from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
from store.controller import authview, cart, wishlist, checkout, order
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name = 'Home' ),
    path('categorys', categorys, name = 'Categorys'),
    path('categorys/<str:slug>', categorysview, name = 'CategorysView' ),
    path('categorys/<str:cat_slug>/<str:prod_slug>', productview, name = 'ProductView'),
    
    path('register/', authview.register, name = 'Register'),
    path('login/', authview.loginRequest, name = 'Login'),
    path('logout/', LogoutView.as_view(), name = 'Logout'),
    
    path('add-to-cart', cart.addToCart, name = 'AddToCart'),
    path('cart/', cart.cartView, name = 'CartView'),
    path('updateQuantity', cart.updateCart, name = 'UpdateCart'),
    path('deleteItemCart/<int:itemCart_id>', cart.deleteItemCart, name = 'DeleteItem'),
    
    path('wishlist/', wishlist.wishlistView, name = 'WishList'),
    path('add-to-wishlist', wishlist.addToWishList, name = 'AddToWishlist'),
    path('delete-wishtlist-item/<int:itemWishlist_id>', wishlist.deleteWishlistItem, name = 'DeleteItemWL'),
    
    path('checkout/', checkout.checkoutView, name = 'CheckoutView'),
    path('place-order', checkout.placeOrder, name = 'PlaceOrder'),
    
    path('my-orders/', order.myOrders, name = 'MyOrders'),
    path('my-orders/<str:tracking_nro>/', order.orderDetail, name = 'OrderDetail'),
    
    path('product-list', productListAjax),
] + static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
