from django.test import TestCase, Client
from django.urls import reverse
from main.models import Korisnik, Trener, Trening

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        self.homepage_url = reverse('homepage')
        self.treneri_q_url = reverse('trener_q', args=['neki-trener'])

        self.trener1 = Trener.objects.create(
            trener_ime = "neki-trener",
            trener_id = "TestniId"
        )

    def test_project_homepage_GET(self):
        client = Client()

        response = client.get(self.homepage_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'base_generic.html')

    def test_project_authors_GET(self):
        client = Client()

        response = client.get(self.treneri_q_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, '')

