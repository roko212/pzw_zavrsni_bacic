from django.db import models
from django.utils import timezone

# Create your models here.

class Korisnik(models.Model):
    korisnik_ime = models.CharField(max_length=50)
    korisnik_datum_rodenja = models.DateField()
    korisnik_mail = models.EmailField()

    def __str__(self):
        return self.korisnik_ime
    
class Trener(models.Model):
    trener_ime = models.CharField(max_length=50)

    def __str__(self):
        return self.trener_ime
    
class Trening(models.Model):
    trening_ime = models.CharField(max_length=20)
    trening_vrsta = models.CharField(max_length=20)
    trening_opis = models.TextField()
    trening_trener = models.ForeignKey(Trener, on_delete=models.CASCADE)
    trening_termin = models.DateTimeField(default=timezone.now)