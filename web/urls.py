from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from main import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name="home"),

    path('demo/', views.demo, name="demo"),
 
    path('naruci/', views.narudzba, name="narudzba"),
   
    path('korisnik/<str:nacin>/', views.racun, name="signup"),
    path('lista/', views.kosarica, name="kosarica"),
    path('kosarica/<str:qry>/<int:jelo>', views.dodaj, name="kosara"),

    path('restoran/<str:ime>/', views.restoran, name="restoran"),
    path('profil/', views.account, name="account"),
]

