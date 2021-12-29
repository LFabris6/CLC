from django.http.response import Http404
from django.contrib.auth.models import User
from django.http import request
from django.shortcuts import  render, redirect
from .forms import NewUserForm, LoginForm, Profil, Upit
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from .models import Korisnik, Narudzba, Restoran, Jelo



def dodaj(request, qry, jelo):

    usr = Korisnik.objects.get(user=request.user)
    for i in usr._meta.get_fields():
        if getattr(usr, i.name) == "":
            messages.error(request, "Molimo vas unesite potrebne podatke")
            return redirect("/profil")
    
    
    jelo = Jelo.objects.get(id=jelo)
    narudzba = Narudzba.objects.get(user=request.user)
    if qry == "dodaj":
        narudzba.meni.add(jelo)
        narudzba.ukupno+=jelo.cijena
        narudzba.save()
        messages.success(request, "Jelo je dodano u vašu košaricu!")
        return redirect("/restoran/"+jelo.restoran.ime)
    if qry == "izbaci":
        narudzba.meni.remove(jelo)
        narudzba.ukupno-=jelo.cijena
        narudzba.save()
        messages.success(request, "Jelo je izbačeno iz košarice")
        return redirect("/lista")

    return Http404
    


def kosarica(request):
    user = request.user
    narudzba =  Narudzba.objects.get(user=request.user)
    
    return render(request, 'main/kosarica.html', {"narudzba":narudzba})

def restoran(request, ime):
    rs = Restoran.objects.get(ime=ime)

    #sav meni:
    jela = rs.jelo_set.all()
    
    
    args = {"rs":rs, "jela":jela}
    return render(request, "main/restoran.html", args)

def narudzba(request):
    usr = Korisnik.objects.get(user=request.user)
    
    for i in usr._meta.get_fields():
        if getattr(usr, i.name) == "":
            messages.error(request, "Molimo vas unesite potrebne podatke")
            return redirect("/profil")
    
    #izlistaj
    nard = Narudzba.objects.get(user=request.user)
    if nard.potvrdeno is False:
        nard.potvrdeno = True
        nard.save()
        messages.success(request, "Hvala vam, Zaprimili smo vašu narudžbu te će biti izvršena u što kraćem roku.")
    else:
        messages.warning(request, "Vaša narudzba već je u tijeku.")
    print("dd")

    
    
    return redirect("/lista/")





def main(request):
    if request.method == "POST":
        form = Upit(request.POST)
        if form.is_valid():
            #startat smtp server
            email = form.cleaned_data.get('email')
            ime = form.cleaned_data.get('ime')
            telefon = form.cleaned_data.get('telefon')
            poruka = form.cleaned_data.get('poruka')
    else:
        form = Upit()


    args = {"form":form}
    return render(request, 'main/main.html', args)

def demo(request):
    restorani = Restoran.objects.filter(grad="Rovinj")
    args = {"restorani":restorani}
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
                    messages.success(request, "Dobro došli!")
                    return redirect('/demo/')
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
                    messages.success(request, "Dobro došli natrag!")
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

