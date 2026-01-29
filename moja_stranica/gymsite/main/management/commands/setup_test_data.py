import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import Korisnik, Trener, Trening
from main.factories import (
    KorisnikFactory,
    TrenerFactory,
    TreningFactory
)

NUM_KORISNICI = 10
NUM_TRENERI = 10
NUM_TRENINZI = 10

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Korisnik, Trener, Trening]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_KORISNICI):
            korisnik = KorisnikFactory()

        for _ in range(NUM_TRENERI):
            trener = TrenerFactory()

        for _ in range(NUM_TRENINZI):
            trening = TreningFactory()