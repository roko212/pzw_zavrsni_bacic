import random

from django.db import transaction
from django.core.management.base import BaseCommand

from main.models import Korisnik, Trener
from main.factories import (
    KorisnikFactory,
    TrenerFactory
)

NUM_KORISNICI = 10
NUM_TRENERI = 10

class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [Korisnik, Trener]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")

        for _ in range(NUM_KORISNICI):
            korisnik = KorisnikFactory()

        for _ in range(NUM_TRENERI):
            trener = TrenerFactory()