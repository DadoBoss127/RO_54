from itertools import product

from django.shortcuts import render, get_object_or_404
from .cart import Cart
from shop.models import Shop
from django.http import JsonResponse

def cart_summary(request):
    cart = Cart(request)
    cart_products = cart.get_prods()
    quantities = cart.get_quants
    return render(request, 'mycart/cart_summary.html', {'cart_products': cart_products, 'quantities': quantities})


def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Shop, id=product_id)

        cart.add(product=product, quantity=product_qty)

        cart_quantity = cart.__len__()
        # response = JsonResponse({'Product Name: ' : product.title, 'Product Price: ' : product.price})
        response = JsonResponse({'qty': cart_quantity})
        return response


def cart_delete(request):
    pass


def cart_update(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = request.POST.get('product_qty')

        cart.update(product=product_id, quantity=product_qty)

        response = JsonResponse({'qty': product_qty})
        return response
        # return redirect('cart_summary')