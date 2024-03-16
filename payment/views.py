from django.shortcuts import render, redirect

from payment.forms import ShippingForm
from payment.models import ShippingAddress


def payment_success(request):
    return render(request, 'payment/payment_succes.html')


def payment_checkout(request):
    if request.user.is_authenticated:
        shipping_user = ShippingAddress.objects.get(id=request.user.id)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        if shipping_form.is_valid():
            shipping_form.save()

            # messages.success(request, 'User updated successfully!')
            return redirect('home-page')
        return render(request, 'payment/payment_checkout.html', {'shipping_form': shipping_form})
    else:
        # messages.success(request, 'You must be logged to access this page.')
        return redirect('home-page')
