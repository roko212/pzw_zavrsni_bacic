from django.contrib import admin
from .models import *

# Register your models here.

model_list = [Korisnik, Trener, Trening]
admin.site.register(model_list)