

from django.contrib.auth.forms import PasswordChangeForm, UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms import ModelForm
from .models import Korisnik, Narudzba

class NewUserForm(UserCreationForm):

    
    class Meta:
        model = User
        fields = ["password1", "password2", "email"]

    def __init__(self, *args, **kwargs):
        super(NewUserForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True

    def save(self, commit=True):
        email = self.cleaned_data["email"]

        user = super(NewUserForm, self).save(commit=False)
        user.email = email
        
        
        
        for i in range(len(email)):
            if(email[i] == "@"):
                name = "".join(email[0:i])
        
        user.username = name
                

        if commit:
            user.save()
            profilna = Korisnik(user=user, drzava="Hrvatska", regija="Istra")
            profilna.save()
            narudzba = Narudzba(user=user)
            narudzba.save()
        return user




class LoginForm(forms.Form):
    email = forms.CharField(max_length=50)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)


class Profil(forms.Form):
    ime = forms.CharField(max_length=50, required=False)
    prezime = forms.CharField(max_length=50, required=False)
    adresa = forms.CharField(max_length=50, required=False)
    telefon= forms.IntegerField(required=False)
    email = forms.CharField(max_length=50, required=False)
    sirina = forms.FloatField(required=False)
    duzina = forms.FloatField(required=False)
    


    def __init__(self, user, *args, **kwargs):
        super(Profil, self).__init__(*args, **kwargs)
        self.user = user
        


        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

        korisnik = Korisnik.objects.get(user=user)
        

        self.fields['ime'].widget.attrs['placeholder'] = self.fields['ime'].label or korisnik.ime
        self.fields['prezime'].widget.attrs['placeholder'] = self.fields['prezime'].label or korisnik.prezime
        self.fields['adresa'].widget.attrs['placeholder'] = self.fields['adresa'].label or korisnik.adresa
        self.fields['telefon'].widget.attrs['placeholder'] = self.fields['telefon'].label or korisnik.telefon
        self.fields['email'].widget.attrs['placeholder'] = self.fields['email'].label or user.email
        self.fields['sirina'].widget.attrs['placeholder'] = self.fields['sirina'].label or korisnik.sirina
        self.fields['duzina'].widget.attrs['placeholder'] = self.fields['duzina'].label or korisnik.duzina


class Upit(forms.Form):
    ime = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=50)
    telefon= forms.IntegerField()
    prouka = forms.TextInput()
