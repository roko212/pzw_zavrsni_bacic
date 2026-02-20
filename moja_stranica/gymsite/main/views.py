from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login
from main.models import *

from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from .forms import *

from django.views.generic import ListView

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



class TreneriList(ListView):
    model = Trener
    template_name = 'main/treneri_list.html'
    context_object_name = 'treneri'

class KorisniciList(ListView):
    model = Korisnik
    template_name = 'main/korisnici_list.html'
    context_object_name = 'korisnici'

class TreninziList(ListView):
    model = Trening
    template_name = 'main/treninzi_list.html'
    context_object_name = 'treninzi'

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

class TrenerCreateView(CreateView):
    model = Trener
    form_class = TrenerForm
    template_name = 'dodaj_trenera.html'
    success_url = reverse_lazy('main:treneri')

class TrenerUpdateView(UpdateView):
    model = Trener
    form_class = TrenerForm
    template_name = 'update_trenera.html'
    success_url = reverse_lazy('main:treneri')

class TrenerDeleteView(DeleteView):
    model = Trener
    template_name = 'delete_trener.html'
    success_url = reverse_lazy('main:treneri')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trener'] = self.get_object()
        return context
    
class TreningCreateView(CreateView):
    model = Trening
    form_class = TreningForm
    template_name = 'dodaj_trening.html'
    success_url = reverse_lazy('main:treninzi')

class TreningUpdateView(UpdateView):
    model = Trening
    form_class = TreningForm
    template_name = 'update_trening.html'
    success_url = reverse_lazy('main:treninzi')

class TreningDeleteView(DeleteView):
    model = Trening
    template_name = 'delete_trening.html'
    success_url = reverse_lazy('main:treninzi')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trening'] = self.get_object()
        return context