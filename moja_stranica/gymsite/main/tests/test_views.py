from django.test import TestCase, Client
from django.urls import reverse
from datetime import date
from django.utils import timezone
from main.models import Korisnik, Trener, Trening

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.homepage_url = reverse('main:index')
        self.treneri_q_url = reverse('main:treneri')
        self.korisnici_url = reverse('main:korisnici')
        self.treninzi_url = reverse('main:treninzi')

        self.trener1 = Trener.objects.create(
            trener_ime = "neki-trener",
            trener_mail = "trener@trener.com",
        )


        self.trening = Trening.objects.create(
            trening_ime = "neki-trening",
            trening_vrsta = "kardio",
            trening_opis = "novi kardio u našoj ponudi",
            trening_trener = self.trener1,
            trening_termin = timezone.now(),
        )

        self.korisnik = Korisnik.objects.create(
            korisnik_ime = "neki-korisnik",
            korisnik_datum_rodenja = date(2000, 1, 1),
            korisnik_mail = "netko@nesto.com",
            korisnik_trening = self.trening,
        )

    def test_project_index_GET(self):
        client = Client()

        response = client.get(self.homepage_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_project_treneri_GET(self):
        client = Client()

        response = client.get(self.treneri_q_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/treneri_list.html')


    def test_project_korisnici_GET(self):
        client = Client()

        response = client.get(self.korisnici_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/korisnici_list.html')

    
    def test_project_treninzi_GET(self):
        client = Client()

        response = client.get(self.treninzi_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'main/treninzi_list.html')