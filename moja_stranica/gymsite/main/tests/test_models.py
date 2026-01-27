from django.test import TestCase
from main.models import Korisnik, Trener, Trening

class TestModels(TestCase):

    def setUp(self):
        self.trener1 = Trener.objects.create(
            trener_ime = "neki-trener",
            trener_id = "TestniId"
        )

    def test_trener(self):
        self.assertEqual(self.trener1.trener_ime, "neki-trener")