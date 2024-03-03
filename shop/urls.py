from django.urls import path

from shop import views

urlpatterns = [
    path('rings_products', views.RingsListView.as_view(), name='rings-products'),
    path('create_product', views.ProductCreateView.as_view(), name='create-product'),
    path('detail_product/<int:pk>/', views.ProductDetailView.as_view(), name='detail-product'),
]

