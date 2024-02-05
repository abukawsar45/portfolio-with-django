from django.urls import path
from products.views import *

app_name = 'products'
urlpatterns = [
    path('', index, name='index'),
    path('create/', create_product, name='create_product'),
    path('delete/<int:pk>', delete_product, name='delete_product')

]
 