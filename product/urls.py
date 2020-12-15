from django.urls import path
from .views import products_list , product_details ,product_add , product_edit

urlpatterns = [
    path('product/',products_list , name= 'products_list'),
    path('product/<int:pk>/',product_details , name= 'product_details'),
    path('product/add/',product_add , name= 'product_add'),
    path('product/edit/<int:pk>/',product_edit , name= 'product_edit'),



    
]