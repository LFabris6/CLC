from django.db import models

from django.contrib.auth.models import User

class Korisnik(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ime = models.CharField(max_length=50, blank=True)
    prezime = models.CharField(max_length=50, blank=True)
    telefon = models.IntegerField(max_length=20, null=True)
    adresa = models.CharField(max_length=50, blank=True)
    sirina = models.DecimalField(decimal_places=10, max_digits=20, null=True)
    duzina = models.DecimalField(decimal_places=10, max_digits=20, null=True)
    regija = models.CharField(max_length=50, blank=True)
    grad = models.CharField(max_length=50, blank=True)
    drzava = models.CharField(max_length=50, blank=True)
