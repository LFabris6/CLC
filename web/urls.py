from django.conf.urls import url
from django.contrib import admin
from django.urls import path

from main import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main, name="home"),
    path('demo/', views.demo, name="demo"),
   
    path('korisnik/<str:nacin>/', views.racun, name="signup"),
    path('korisnici/<str:username>/', views.account, name="account"),
]
