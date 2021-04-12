from django.urls import path,include
from .views import *
app_name = "ecom"
urlpatterns = [
    path('',home, name='homepage'),
    path('cart/',cart,name='cart'),
    path('deletecart/<int:pk>/',deletecart,name='deletecart'),
    path('product/<slug:product>/',single_post,name='single_post'),
    path('addtocart/<int:id>/',addtocart,name='addtocart'),
    path('checkout/',checkout,name='checkout'),
    path('checkoutbilling/',checkoutbilling,name='checkoutbilling'),
    path('category/<slug:cat_name>/',category,name='category'),
    path('search/',searchProduct,name='search')
]