from django.urls import path
from product.views import ProductView, ProductAddView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('', ProductView.as_view(), name='products'),
    path('add/', ProductAddView.as_view(), name='add-product'),
    path('update/<str:product_id>', ProductUpdateView.as_view(), name='update-product'),
    path('delete/<str:product_id>', ProductDeleteView.as_view(), name='delete-product'),
]
