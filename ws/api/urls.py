from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('signup/', views.SignupViewDef, name='register'),
    path('login/', views.LoginViewDef, name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('products/', views.ProductViewDef, name='order'),
    path('product/<int:pk>/', views.ProductChangeDeleteDef, name='orderchange'),
    path('product/', views.ProductAddViewDef, name='orderadd'),
    path('cart/', views.CartViewDef, name='cart'),
    path('cart/<int:pk>', views.AddToCartView, name='cartdetail'),
    path('order/', views.GetCreateOrderView, name='orderview'),
]
