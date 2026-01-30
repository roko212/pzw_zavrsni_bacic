from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from main.models import Trener, Korisnik, Trening

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import KorisnikForm

# Create your views here.
def homepage(request):
    return HttpResponse('Dobrodošli na početnu stranicu <strong> GymSpace </strong> teretane!')

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('main:index')

    else:
        form = UserCreationForm()

    context = {'form': form}

    return render(request, 'registration/register.html', context)

def svi_treneri(request):
    treneri = Trener.objects.all()

    context = {'treneri': treneri}

    return render(request, 'treneri.html', context=context)

def svi_korisnici(request):
    korisnici = Korisnik.objects.all()

    context = {'korisnici': korisnici}

    return render(request, 'korisnici.html', context=context)


def svi_treninzi(request):
    treninzi = Trening.objects.all()

    context = {'treninzi': treninzi}

    return render(request, 'treninzi.html', context=context)

class KorisnikCreateView(CreateView):
    model = Korisnik
    form_class = KorisnikForm
    template_name = 'dodaj_korisnika.html'
    success_url = reverse_lazy('main:korisnici')

class KorisnikDeleteView(DeleteView):
    model = Korisnik
    template_name = 'delete_korisnik.html'
    success_url = reverse_lazy('main:korisnici')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['korisnik']=self.get_object()
        return context
    
class KorisnikUpdateView(UpdateView):
    model = Korisnik
    form_class = KorisnikForm
    template_name = 'update_korisnik.html'
    success_url = reverse_lazy('main:korisnici')
