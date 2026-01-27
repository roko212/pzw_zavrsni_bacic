## factories.py
import factory
from factory.django import DjangoModelFactory

from main.models import *

class KorisnikFactory(DjangoModelFactory):
    class Meta:
        model = Korisnik

    korisnik_ime = factory.Faker("first_name")
    korisnik_datum_rodenja = factory.Faker("date_of_birth")
    korisnik_id = factory.Faker("random_int")
    korisnik_mail = factory.Faker("email")

class TrenerFactory(DjangoModelFactory):
    class Meta:
        model = Trener

    trener_ime = factory.Faker("first_name")
    trener_id = factory.Faker("random_int")