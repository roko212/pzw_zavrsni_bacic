from django.test import TestCase
from datetime import date
from django.utils import timezone
from main.models import Korisnik, Trener, Trening

class TestModels(TestCase):

    def setUp(self):
        self.trener1 = Trener.objects.create(
            trener_ime = "neki-trener",
            trener_mail = "netko@trener.com"
        )

        
        self.trening = Trening.objects.create(
            trening_ime = "neki-trening",
            trening_vrsta = "kardio",
            trening_opis = "lagani kardio za buđenje",
            trening_trener=self.trener1,
            trening_termin=timezone.now()
        )


        self.korisnik = Korisnik.objects.create(
            korisnik_ime = "neki-korisnik",
            korisnik_datum_rodenja = date(2000, 5, 20),
            korisnik_mail="netko@nesto.com",
            korisnik_trening = self.trening,
        )

    def test_trener(self):
        self.assertEqual(self.trener1.trener_ime, "neki-trener")

    def test_korisnik(self):
        self.assertEqual(self.korisnik.korisnik_ime, "neki-korisnik")
        self.assertEqual(self.korisnik.korisnik_datum_rodenja, date(2000, 5, 20))
        self.assertEqual(self.korisnik.korisnik_mail, "netko@nesto.com")

    def test_trening(self):
        self.assertEqual(self.trening.trening_ime, "neki-trening")
        self.assertEqual(self.trening.trening_vrsta, "kardio")
        self.assertEqual(self.trening.trening_opis, "lagani kardio za buđenje")
        self.assertEqual(self.trening.trening_trener, self.trener1)
        self.assertIsNotNone(self.trening.trening_termin)