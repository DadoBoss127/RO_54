from django.urls import path

from shop import views
from shop.views import view_cart, product_detail

urlpatterns = [
    path('rings_products', views.RingsListView.as_view(), name='rings-products'),
    path('create_product', views.ProductCreateView.as_view(), name='create-product'),
    path('detail_product/<int:pk>/', views.ProductDetailView.as_view(), name='detail-product'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    path('view-cart/', view_cart, name='view_cart'),
]

#Am adaugat o modificare
