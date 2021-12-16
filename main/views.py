
from django.http.response import Http404
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import  render, redirect
from .forms import NewUserForm, LoginForm, Profil
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import Korisnik



def narudzba(request):
    usr = Korisnik.objects.get(user=request.user)
    
    for i in usr._meta.get_fields():
        if getattr(usr, i.name) == "":
            messages.error(request, "Molimo vas unesite potrebne podatke")
            return redirect("/profil")
    
    messages.success(request, "Hvala vam, zaprimili smo vašu narudžbu, biti će izvršena u što kraćem roku!")
    return redirect("/demo")


def test(request):
    usr = Korisnik.objects.get(user=request.user)
    
    for i in usr._meta.get_fields():
        if getattr(usr, i.name) == "":
            messages.error(request, "Molimo vas unesite potrebne podatke")
            return redirect("/profil")
    
    messages.success(request, "Hvala vam, zaprimili smo vašu narudžbu, biti će izvršena u što kraćem roku!")


    args = {}
    return render(request, 'main/test.html', args)



def main(request):
    args = {}
    return render(request, 'main/main.html', args)

def demo(request):
    
    args = {}
    return render(request, 'main/demo.html', args)

def racun(request, nacin):
    
    
    if nacin == "registracija":

        if request.method == 'POST':
            form = NewUserForm(request.POST)
            if form.is_valid():
                

                email = form.cleaned_data.get('email')
                pswd1 = form.cleaned_data.get('password1')
                
                if(User.objects.filter(email=email).exists() is False):
                    form.save()
                    for i in range(len(email)):
                        if(email[i] == "@"):
                            username = "".join(email[0:i])
                            
                    user = authenticate(username=username, password=pswd1)
                    login(request, user)
                    return redirect('/')
                else:
                    messages.error(request, "Korisnik sa tom email adresom je već registriran!")
            else:
                messages.error(request, "Lozinke se ne podudaraju." )


        else:          
            form = NewUserForm()



        args = {"form":form}
        return render(request, 'main/signup.html', args)
        
        
    elif nacin == "prijava":
       
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                
                email = form.cleaned_data['email']
                for i in range(len(email)):
                    if(email[i] == "@"):
                        username = "".join(email[0:i])
                
                
                user = authenticate(
                username=username,
                password=form.cleaned_data['password'],
                )
                
                if user is not None:
                    
                    login(request, user)
                    return redirect('/demo')
                else:
                    messages.error(request, "Pogrešna lozinka ili email adresa" )

        
                   
        else:
            form = LoginForm()

        args = {"form": form}
        return render(request, 'main/signin.html', args)

    elif nacin=="odjava":

        logout(request)
        return redirect("/demo")

    
    raise Http404
    
polja = ["ime", "prezime", "adresa", "telefon", "sirina", "duzina"]

def account(request):

    usr = Korisnik.objects.get(user=request.user)
    user = request.user
    
    if(request.method=='POST'):
        form = Profil(request.user, request.POST)
        if form.is_valid():
            print(request)
            
            for i in polja:
                izmjena = form.cleaned_data[i]
                if(izmjena):            
                    print(izmjena)        
                    usr.__setattr__(i, izmjena)
                    usr.save()
                   

            
            return redirect('/profil/')
    else:
        form = Profil(request.user)

    
    args = {'korisnik':usr, "form":form}
    return render(request, 'main/acc.html', args)

