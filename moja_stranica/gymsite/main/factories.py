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

class TreningFactory(DjangoModelFactory):
    class Meta:
        model = Trening

    trening_ime = factory.Faker("word")
    trening_vrsta = factory.Faker(
        "random_element",
        elements=["kardio", "snaga", "funkcionalni", "yoga", "HIIT"]
    )
    trening_opis = factory.Faker("paragraph", nb_sentences=3)
    trening_trener = factory.SubFactory(TrenerFactory)
    trening_termin = factory.Faker('date_time')