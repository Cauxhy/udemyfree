# products/urls.py

from django.urls import path
from .views import home,product_list, product_detail,how_to_use

urlpatterns = [
    path('', home, name='home'),
    path('courses', product_list, name='product_list'),
    path('how-to-use', how_to_use, name='how_to_use'),
    path('product/<int:pk>/', product_detail, name='product_detail'),
]
