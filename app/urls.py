from django.urls import path
from .views import *
urlpatterns = [
   
    path('', home, name='home'),
    path('login/', loginuser),
    path('register/', register,name='register'),
    path('dashbaord/<pk>/', dashbaord,name='dashboard'),
    path('asset/<pk>/', asset,name='asset'),
    path('assets/<pk>/', asset,name='asset'),
    path('withdrawl/<pk>/', withdrawl,name='withdrawl'),
    path('deposite/<pk>/', deposite,name='deposite'),
    path('content-wallet/', contentwallet, name='content-wallet'),
    path('connect-wallet/', contentwallet, name='content-wallet'),
    path('profile/<pk>/', profile, name='profilemain'),
    path('profilemain/', update_profile, name='update_profile'),
    path('password/', change_password, name='change_password'),
    path('add_wallet/', add_wallet , name='add-wallet')
]