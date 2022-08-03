from django.http import JsonResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from store.models import WishList, Product
from django.contrib.auth.decorators import login_required

def wishlistView(request):
    wishlist = WishList.objects.filter(user = request.user)
    context = {'wishlist' : wishlist}
    return render(request, 'store/wishlist.html', context)

@login_required()
def addToWishList(request):
    if request.method == 'POST':
        prod_id = int(request.POST.get('product_id'))
        product_check = Product.objects.get(id = prod_id)
        if product_check:
            if WishList.objects.filter(user_id = request.user.id, product_id = prod_id):
                return JsonResponse({'status': 'Product Already in Wishlist'})
            else:
                WishList.objects.create(user = request.user, product_id = prod_id)
                return JsonResponse({'status': 'Product Added in Wishlist'})
        else:
            return JsonResponse({'status': 'No such product found'})
    return redirect('/')

def deleteWishlistItem(request, itemWishlist_id):
    item = WishList.objects.get(id = itemWishlist_id, user_id = request.user)
    item.delete()
    messages.warning(request, 'Product remove from Whislist')
    
    return redirect('WishList')