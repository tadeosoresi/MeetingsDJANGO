from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Meetings import views

urlpatterns = [
    path('home', views.home, name='index'),
    path('shop', views.shop, name='shop'),
    path('us', views.nosotros, name='nosotros'),
    path('register', views.register, name='registro'),
    path('hidden', views.hidden, name='hidden'),
    path('rooftop', views.rooftop, name='rooftop'),
    path('modern', views.modern, name='modern'),
    path('woman', views.woman, name='woman'),
    path('mason', views.mason, name='mason'),
    path('conglomerate', views.conglomerate, name='conglomerate'),
    path('tienda', views.tienda, name='tienda'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)