from django.urls import path, include
from . import views

from django.views.generic import ListView
from main.models import *

from main.views import *

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('treneri/', views.svi_treneri, name='treneri'),
    path('korisnici/', views.svi_korisnici, name='korisnici'),
    path('treninzi/', views.svi_treninzi, name='treninzi'),
    path('dodaj-korisnika/', views.KorisnikCreateView.as_view(), name='dodaj_korisnika'),
    path('obrisi-korisnika/<int:pk>/', views.KorisnikDeleteView.as_view(), name='obrisi_korisnika'),
    path('update-korisnika/<int:pk>/', views.KorisnikUpdateView.as_view(), name='update_korisnika'),
]