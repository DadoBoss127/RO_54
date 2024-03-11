from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.decorators.http import require_POST
from django.views.generic import ListView, CreateView, DetailView

from shop.forms import ShopForm, AddToCartForm
from shop.models import Shop


class RingsListView(ListView):
    template_name = 'rings/shop_list_rings.html'
    model = Shop
    context_object_name = 'all_rings_items'

    def get_queryset(self):
        return Shop.objects.filter(type='rings').order_by('-created_at')


class ProductCreateView(CreateView):
    template_name = 'shop/create_product.html'
    model = Shop
    form_class = ShopForm
    success_url = reverse_lazy('home-page')

#Am creat un views nou

class ProductDetailView(DetailView):
    model = Shop
    template_name = 'shop/details_product.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = self.object
        return context


def search(request):
    pass


