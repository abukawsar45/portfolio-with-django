from django.urls import path
from products.views import *

app_name = 'products'
urlpatterns = [
    path('', index, name='index'),
    path('create/', create_product, name='create_product'),
    path('detail/<int:pk>/', product_details, name='product_details'),
    path('update/<int:pk>', update_product, name='update_product'),
    path('delete/<int:pk>', delete_product, name='delete_product')

]
 