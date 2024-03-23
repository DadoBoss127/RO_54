from django.shortcuts import render, redirect

from cart.cart import Cart
from payment.forms import ShippingForm
from payment.models import ShippingAddress


def payment_success(request):
    return render(request, 'payment/payment_succes.html')


def payment_checkout_form(request):
    if request.user.is_authenticated:
        profile = request.user.profile
        shipping_user, created = ShippingAddress.objects.get_or_create(user=profile)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        if shipping_form.is_valid():
            shipping_form.save()
            return redirect('home-page')
        return render(request, 'payment/payment_checkout.html', {'shipping_form': shipping_form})
    else:
        return redirect('home-page')


def payment_checkout(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = ShippingForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)  # Don't save yet
            order.user = request.user.profile  # Add user association if applicable
            order.save()
            cart.clear()
            return redirect('home-page')
    else:
        form = ShippingForm()
    context = {'form': form}
    return render(request, 'payment/payment_checkout.html', context)
