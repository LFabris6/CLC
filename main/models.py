
from django.db import models

from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, DO_NOTHING



class Restoran(models.Model):
    ime = models.CharField(max_length=50, blank=True)
    kratko = models.TextField(blank=True)
    opis = models.TextField(blank=True)
    sirina = models.FloatField(null=True)
    duzina = models.FloatField(null=True)
    grad = models.CharField(max_length=50, blank=True)
    slika = models.ImageField(default = "static/img/default1.jpg", upload_to='static/user/')

    def __str__(self):
        return 'Restoran: ' + self.ime
    

class Jelo(models.Model):
    ime = models.CharField(max_length=50, blank=True)
    cijena = models.IntegerField(null=True)
    restoran = models.ForeignKey(Restoran, on_delete=models.CASCADE, null = True)
    slika = models.ImageField(default = "static/img/default1.jpg", upload_to='static/user/')

    def __str__(self):
        return self.ime
    

    
class Korisnik(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ime = models.CharField(max_length=50, blank=True)
    prezime = models.CharField(max_length=50, blank=True)
    telefon = models.IntegerField(null=True)
    adresa = models.CharField(max_length=50, blank=True)
    sirina = models.FloatField(null=True)
    duzina = models.FloatField(null=True)
    regija = models.CharField(max_length=50, blank=True)
    drzava = models.CharField(max_length=50, blank=True)

    def __str__(self):
        return self.user.username

    

    
    
class Narudzba(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    meni = models.ManyToManyField(Jelo, blank=True)
    ukupno = models.IntegerField(default=0)
    potvrdeno = models.BooleanField(default=False)
    

    def __str__(self):
        return self.user.username
    
