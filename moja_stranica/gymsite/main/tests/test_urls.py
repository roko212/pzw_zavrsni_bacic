from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import *

class TestUrls(SimpleTestCase):

    def test_index_url_is_resolved(self):
        url = reverse('main:index')
        #print(resolve(url))

        self.assertEqual(resolve(url).func, index)


    def test_register_url_is_resolved(self):
        url = reverse('main:register')

        self.assertEqual(resolve(url).func, register)


    def test_treneri_url_is_resolved(self):
        url = reverse('main:treneri')

        self.assertEqual(resolve(url).func.view_class, TreneriList)

    def test_korisnici_url_is_resolved(self):
        url = reverse('main:korisnici')

        self.assertEqual(resolve(url).func.view_class, KorisniciList)

    
    def test_treninzi_url_is_resolved(self):
        url = reverse('main:treninzi')

        self.assertEqual(resolve(url).func.view_class, TreninziList)
    