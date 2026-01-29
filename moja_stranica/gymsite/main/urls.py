from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('treneri/', views.svi_treneri, name='treneri'),
    path('korisnici/', views.svi_korisnici, name='korisnici'),
    path('treninzi/', views.svi_treninzi, name='treninzi')
]