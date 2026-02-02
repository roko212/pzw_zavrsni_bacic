from django.test import TestCase, Client
from django.urls import reverse
from main.models import Korisnik, Trener, Trening

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.homepage_url = reverse('main:index')
        self.treneri_q_url = reverse('main:treneri')

        self.trener1 = Trener.objects.create(
            trener_ime = "neki-trener",
        )

    def test_project_index_GET(self):
        client = Client()

        response = client.get(self.homepage_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_project_korisnici_GET(self):
        client = Client()

        response = client.get(self.treneri_q_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'treneri.html')



    

