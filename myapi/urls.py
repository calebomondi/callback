from django.urls import path
from . import views

urlpatterns = [
    path('',views.welcome,name='home-page'),
    path('show/',views.show,name='show'),
    path('stkpush/', views.initiate_payment, name='initiate_payment'),
    path('callback/', views.mpesa_callback, name='mpesa_callback'),
]