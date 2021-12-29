from django.contrib import admin

from .models import Korisnik, Restoran, Jelo, Narudzba

admin.site.register(Korisnik)
admin.site.register(Restoran)
admin.site.register(Jelo)
admin.site.register(Narudzba)

