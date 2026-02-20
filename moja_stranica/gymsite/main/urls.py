from django.urls import path, include
from . import views

from django.views.generic import ListView
from main.models import *

from main.views import *

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('treneri/', TreneriList.as_view(), name='treneri'),
    path('korisnici/', KorisniciList.as_view(), name='korisnici'),
    path('treninzi/', TreninziList.as_view(), name='treninzi'),
    path('dodaj-korisnika/', views.KorisnikCreateView.as_view(), name='dodaj_korisnika'),
    path('obrisi-korisnika/<int:pk>/', views.KorisnikDeleteView.as_view(), name='obrisi_korisnika'),
    path('update-korisnika/<int:pk>/', views.KorisnikUpdateView.as_view(), name='update_korisnika'),
    path('dodaj-trenera/', views.TrenerCreateView.as_view(), name='dodaj_trenera'),
    path('update-trenera/<int:pk>/', views.TrenerUpdateView.as_view(), name='update_trenera'),
    path('obrisi-trenera/<int:pk>/', views.TrenerDeleteView.as_view(), name='obrisi_trenera'),
    path('dodaj-trening/', views.TreningCreateView.as_view(), name='dodaj_trening'),
    path('obrisi-trening/<int:pk>/', views.TreningDeleteView.as_view(), name='obrisi_trening'),
    path('update-trening/<int:pk>/', views.TreningUpdateView.as_view(), name='update_trening'),
]