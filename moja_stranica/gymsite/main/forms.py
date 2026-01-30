from django import forms
from .models import *

class KorisnikForm(forms.ModelForm):
    class Meta:
        model = Korisnik
        fields = ['korisnik_ime', 'korisnik_datum_rodenja', 'korisnik_mail']
        widgets = {
            'korisnik_datum_rodenja': forms.DateInput(attrs={'type': 'date'})
        }