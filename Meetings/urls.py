from django.urls import path
from Meetings import views

urlpatterns = [
    path('home', views.home, name='index'),
    path('shop', views.shop, name='shop'),
    path('register', views.register, name='registro'),
    path('hnas', views.hidden, name='hidden'),
    path('rooftop', views.rooftop, name='rooftop'),
]