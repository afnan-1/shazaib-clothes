
from django.urls import path,include
from .views import *
urlpatterns = [
    path('signup/',signup_view, name='signup'),
    path('login/',login_user, name='login'),
    path('profile/',profile,name='profile'),
    path('editprofile/',edit_profile,name='editprofile'),
    path('logout/',logout_view,name='logout'),
    path('orders/',orders,name='name')
]