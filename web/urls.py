from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from main import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name="home"),
    path('test/', views.test, name="home"),
    path('demo/', views.demo, name="demo"),
   
    path('korisnik/<str:nacin>/', views.racun, name="signup"),
    path('profil/', views.account, name="account"),
]
