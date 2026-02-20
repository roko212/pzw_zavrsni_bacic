from django import forms
from .models import *

class KorisnikForm(forms.ModelForm):
    class Meta:
        model = Korisnik
        fields = ['korisnik_ime', 'korisnik_datum_rodenja', 'korisnik_mail', 'korisnik_trening']
        widgets = {
            'korisnik_datum_rodenja': forms.DateInput(attrs={'type': 'date'})
        }


class TrenerForm(forms.ModelForm):
    class Meta:
        model = Trener
        fields = ['trener_ime', 'trener_mail']
        widgets = {}

class TreningForm(forms.ModelForm):
    class Meta:
        model = Trening
        fields = ['trening_ime', 'trening_vrsta', 'trening_opis', 'trening_trener', 'trening_termin']
        widgets = {
            'trening_termin': forms.DateTimeInput(attrs={"type": "datetime-local", "class": "form-control"})
        }