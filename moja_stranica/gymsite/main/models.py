from django.db import models
from django.utils import timezone

# Create your models here.
    
class Trener(models.Model):
    trener_ime = models.CharField(max_length=50)
    trener_mail = models.EmailField()

    def __str__(self):
        return self.trener_ime
    
class Trening(models.Model):

    vrste_treninga = [("kardio", "Kardio"), ("snaga", "Snaga"), ("funkcionalni", "Funkcionalni"), ("HIIT", "hiit"), ("yoga", "Yoga")]

    trening_ime = models.CharField(max_length=20)
    trening_vrsta = models.CharField(max_length=20, choices=vrste_treninga)
    trening_opis = models.TextField()
    trening_trener = models.ForeignKey(Trener, on_delete=models.CASCADE)
    trening_termin = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.trening_ime
    

class Korisnik(models.Model):
    korisnik_ime = models.CharField(max_length=50)
    korisnik_datum_rodenja = models.DateField()
    korisnik_mail = models.EmailField()
    korisnik_trening = models.ForeignKey(Trening, on_delete=models.CASCADE)

    def __str__(self):
        return self.korisnik_ime