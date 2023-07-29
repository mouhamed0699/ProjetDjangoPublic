from telnetlib import LOGOUT
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from requests import request
from .models import Chambres, Client, FactureChambre, FactureVoiture, ReservationVoiture,Vol,Hotel,Ville,ReservationChambre
from datetime import datetime
from django.shortcuts import render
from django.db import connection
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate, login,logout
# Create your views here.
def index(request):
    prenom = request.session.get('prenom')  # Récupérer la valeur de 'prenom' du contexte de session
    context = {'prenom': prenom}
    return render(request,'index.html',context)

def connexion(request):
    if request.method == "POST":
        email = request.POST.get('email')
        passWord = request.POST.get('password')
        
        try:
            client = Client.objects.get(email=email)
            
            if client.PassWord == passWord:
                reservationC = ReservationChambre.objects.filter(id_client_id=client.id_client).first()
                factureC = None
                chambre = None
                
                if reservationC:
                    factureC = FactureChambre.objects.get(num_reservation_id=reservationC.num_reservation)
                    chambre = Chambres.objects.get(id_chambre=reservationC.id_chambre_id)
                
                request.session['user_id'] = client.id_client
                request.session['prenom'] = client.prenom
                
                if reservationC:
                    request.session['montant'] = factureC.montant
                    request.session['Num'] = reservationC.id_chambre_id
                    request.session['image'] = chambre.image
                
                return redirect('index')
            else:
                erreur_message = "Identifiants invalides. Veuillez vérifier votre e-mail et votre mot de passe."
                context = {"erreur_message": erreur_message}
                return render(request, 'connexion.html', context)
        except Client.DoesNotExist:
            erreur_message = "Identifiants invalides. Veuillez vérifier votre e-mail et votre mot de passe."
            context = {"erreur_message": erreur_message}
            return render(request, 'connexion.html', context)
    
    return render(request, 'connexion.html')


def deconnexion(request):
    logout(request)
    return redirect('index')

def deconnexionChambre(request):
    logout(request)
    return redirect('chambres')

  
from django.core.exceptions import ObjectDoesNotExist

def inscription(request):
    form = UserCreationForm(request.POST)
    context = {'form': form}
    
    if request.method == 'POST':
        prenom = request.POST.get('prenom')
        nom = request.POST.get('nom')
        email = request.POST.get('email')
        tel = request.POST.get('tel')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        
        try:
            client = Client.objects.get(email=email)
            erreur_message = 'Cet e-mail existe déjà.'
            context['erreur'] = erreur_message
            return render(request, 'inscription.html', context)
        except ObjectDoesNotExist:
            if password1 == password2:
                nouveau_client = Client(
                    nom=nom,
                    prenom=prenom,
                    telephone=tel,
                    email=email,
                    PassWord=password1
                )
                nouveau_client.save()
                return redirect('connexion')
    
    return render(request, 'inscription.html', context)



def voiture(request):
    prenom = request.session.get('prenom')  # Récupérer la valeur de 'prenom' du contexte de session
    context = {'prenom': prenom}
   
    return render(request, 'voiture.html',context)

def chambres(request):
    prenom = request.session.get('prenom')  # Récupérer la valeur de 'prenom' du contexte de session
    context = {'prenom': prenom}
    return render(request, 'chambres.html',context)

def vol(request):
    prenom = request.session.get('prenom')  # Récupérer la valeur de 'prenom' du contexte de session
    context = {'prenom': prenom}
    return render(request, 'vol.html',context)

def recherche_vols(request):
    destination = request.GET.get('destination')
    date_depart = request.GET.get('date_depart')

    # Convertir la date de départ en objet datetime si nécessaire
    date_depart = datetime.strptime(date_depart, '%Y-%m-%d').date()

    # Effectuer la recherche dans la base de données
    vols_disponibles = Vol.objects.filter(aeroport_arrivee__nom=destination, date_depart__date=date_depart)

    # Afficher les résultats
    context = {
        'vols_disponibles': vols_disponibles
    }
    return render(request, 'recherche.html', context)


from django.db import connection
from django.shortcuts import render

def rechercher_chambre(request):
    prenom = request.session.get('prenom')  # Récupérer la valeur de 'prenom' du contexte de session
    print(prenom)
    context = {'prenom': prenom}
    if request.method == "POST":
        ville = request.POST.get('ville')
        hotel = request.POST.get('hotel')
        type_chambre = request.POST.get('type')
        prix = request.POST.get('prix')
        min_prix, max_prix = map(int, prix.split("-"))

        with connection.cursor() as cursor:
            query = """
                SELECT ac.id_chambre, ac.montant, ah.nom,ac.image
                FROM AppliDjango_chambres ac 
                INNER JOIN AppliDjango_hotel ah ON ah.id_hotel = ac.id_hotel_id 
                INNER JOIN AppliDjango_ville av ON av.id_ville = ah.id_ville_id 
                INNER JOIN AppliDjango_typechambre atc ON atc.id_typeChambre = ac.id_typeChambre_id 
                WHERE av.nom = %s AND atc.type = %s AND ac.montant BETWEEN %s AND %s AND ah.nom LIKE %s
            """
            cursor.execute(query, [ville, type_chambre, min_prix, max_prix, '%' + hotel + '%'])
            chambre_disponible = cursor.fetchall()

        context = {'chambre_disponible': chambre_disponible}
        return render(request, 'rechercheChambre.html', context)
    return render(request, 'rechercheChambre.html',context)

# def charger_ville(request):
#     villes = Ville.objects.all()
#     context = {'villes': villes}
#     return render(request, 'chambres.html', context)
    
# def charger_hotel(request):
#     hotels = Hotel.objects.all()  
#     context = {'hotels': hotels}
#     return render(request, 'chambres.html', context)


def rechercher_voiture(request):
    if request.method == "POST":
        marque = request.POST.get('Marque')
        prix = request.POST.get('Prix')
        min_prix, max_prix = map(int, prix.split("-"))
        print(max_prix,min_prix)
        with connection.cursor() as cursor:
            query = """
                    SELECT amvv.nom, av.montant, amv.nom, image,vin
                    FROM AppliDjango_voiture av,AppliDjango_modelevoiture amv,AppliDjango_marquevoiture amvv
                    WHERE av.id_modele_id = amv.id_modele AND amv.id_marque_id = amvv.id_marque 
                    AND amvv.nom = %s  AND av.montant BETWEEN %s AND %s
            """
            cursor.execute(query, [marque, min_prix, max_prix])
            voitures_disponibles = cursor.fetchall()

            context = {'voitures_disponibles': voitures_disponibles}
        return render(request, 'rechercher_voiture.html', context)
    
    
from django.contrib.auth.decorators import login_required
# @login_required 
def reservationChambre(request):
    if request.method=="POST":
        prenom=request.POST.get("prenom")
        nom=request.POST.get("nom")
        email=request.POST.get("email")
        DateArrive=request.POST.get("checkin")
        Duree=request.POST.get("duree")
        Num=request.POST.get("Num")
        Montant=request.POST.get("Montant")
        print(nom,email,prenom)
        
        try:
            
            utilisateur=Client.objects.get(email=email)
            new_reservation=ReservationChambre(
                date_reservation=DateArrive,
                duree=Duree,
                id_client_id=utilisateur.id_client,
                id_chambre_id=Num
            )

            new_reservation.save()
            new_facture=FactureChambre(
                montant=Montant,
                date_facture=DateArrive,
                num_reservation=new_reservation
                
            )
            new_facture.save()
            return redirect('chambres')
        except ObjectDoesNotExist:
            message_erreur="Veillez vous inscrire"
            context={'message_erreur':message_erreur}
            return render(request,'rechercheChambre.html',context)
    message = "Veuillez vous connecter pour effectuer une réservation."
    context = {'message': message}
    return render(request, 'rechercheChambre.html', context)
        
def rechercher_vol(request):
    if request.method == "POST":
        depart = request.POST.get('depart')
        date_dep = request.POST.get('date_dep')
        date_ret = request.POST.get('date_ret')
        destination = request.POST.get('destination')

        with connection.cursor() as cursor:
            query = """
                select time(v.date_depart),time(v.date_arrive),date(v.date_depart),date(v.date_arrive),substring(a1.nom,1,35),substring(a2.nom,1,35),vi1.nom,vi2.nom,v.montant
                from AppliDjango_vol v
                join AppliDjango_aeroport as a1 on v.aeroport_depart_id = a1.id_aeroport
                join AppliDjango_aeroport as a2 on v.aeroport_arrivee_id = a2.id_aeroport
                JOIN AppliDjango_ville AS vi1 ON a1.id_ville_id = vi1.id_ville
                JOIN AppliDjango_ville AS vi2 ON a2.id_ville_id = vi2.id_ville
                WHERE vi1.nom like %s and  vi2.nom like %s 
                and DATE_FORMAT(DATE(v.date_depart), '%%Y-%%m-%%d') = %s 
            """
            cursor.execute(query, [ '%'+depart+'%', '%'+destination+'%' ,date_dep ])
            vols = cursor.fetchall()

        context = {'vols': vols}
        return render(request, 'rechercheVol.html', context)
    



def login_view(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'connexion.html', {'error': 'Identifiants invalides'})

    return render(request, 'connexion.html')

def reservationVoiture(request):
    if request.method=="POST":
        prenom=request.POST.get("prenom")
        nom=request.POST.get("nom")
        email=request.POST.get("email")
        DateReservation=request.POST.get("DateRs")
        DateRen=request.POST.get("DateRt")
        Num=request.POST.get("Num")
        print(nom,email,prenom)
        Montant=request.POST.get("Montant")
        Num=request.POST.get("Num")
        
        try:
            
            utilisateur=Client.objects.get(email=email)
            new_facture=FactureVoiture(
                date_facture=DateReservation,
                montant=Montant,
            )
            new_facture.save()
            new_reservation=ReservationVoiture(
                date_reservation=DateReservation,
                 date_retour=DateRen,
                 id_client_id=utilisateur.id_client,
                 vin_id=Num,
                 id_facture=new_facture,    
            )
            new_reservation.save()
            return redirect('voiture')
        except ObjectDoesNotExist:
            message_erreur="Veillez vous inscrire"
            context={'message_erreur':message_erreur}
            return render(request,'rechercheChambre.html',context)

def Profil(request):
    user_id = request.session.get('user_id')
    prenom = request.session.get('prenom')  # Récupérer la valeur de 'prenom' du contexte de session
    print(user_id)
    reservations = ReservationChambre.objects.filter(id_client_id=user_id)
    images = []
    numeros = []
    montants = []
    print(reservations)
    for reservation in reservations:
        chambre = Chambres.objects.get(id_chambre=reservation.id_chambre_id)
        print(chambre)
        facture = FactureChambre.objects.get(num_reservation_id=reservation.num_reservation)
        images.append(chambre.image)
        numeros.append(reservation.id_chambre_id)
        montants.append(facture.montant)
    print(montants,images,numeros)
    context = {
        'prenom': prenom,
        'images': images,
        'numeros': numeros,
        'montants': montants,
        'reservations': zip(numeros, images, montants)
    }
    
    return render(request, "Profil.html", context)

def Delette(request):
    if request.method=="POST":
        numero=request.POST.get("numero")
        
        try:
            reservation=ReservationChambre.objects.get(id_chambre=numero)
            print(reservation.id_chambre)
            reservation.delete()
            return redirect('Profil')
        except:
            pass
        
        return render(request,'Profil.html')