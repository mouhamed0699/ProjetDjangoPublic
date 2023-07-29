from aifc import Error
import random
from django.conf import settings
from django.db import models

# Create your models here.

# creons la classe aeraport
import os
from django.core.files import File
from django.db import models
from datetime import datetime, timedelta

from Project1.settings import BASE_DIR

class Client(models.Model):
    id_client = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    telephone = models.CharField(max_length=30)
    email = models.CharField(max_length=50,unique=True)
    PassWord=models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nom} {self.prenom}"


class Operateur(models.Model):
    id_operateur = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=30)

    def __str__(self):
        return self.nom


class TypeChambre(models.Model):
    id_typeChambre = models.AutoField(primary_key=True)
    type = models.CharField(max_length=50)

    def __str__(self):
        return self.type


class Ville(models.Model):
    id_ville = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class Hotel(models.Model):
    id_hotel = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    id_ville = models.ForeignKey(Ville, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Chambres(models.Model):
    id_chambre = models.AutoField(primary_key=True)
    montant = models.IntegerField()
    id_hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    id_typeChambre = models.ForeignKey(TypeChambre, on_delete=models.CASCADE)
    image=models.CharField(max_length=200)

    def __str__(self):
        return f"Chambre {self.id_chambre}"

class ReservationChambre(models.Model):
    num_reservation = models.AutoField(primary_key=True)
    date_reservation = models.DateField()
    duree = models.IntegerField()
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_chambre = models.ForeignKey(Chambres, on_delete=models.CASCADE)

    def __str__(self):
        return f"Réservation {self.num_reservation}"

class FactureChambre(models.Model):
    id_facture = models.AutoField(primary_key=True)
    montant = models.IntegerField()
    date_facture = models.DateField()
    num_reservation=models.ForeignKey(ReservationChambre,on_delete=models.CASCADE)
    
    def __str__(self):
        return f"Facture {self.id_facture}"





class Compagnie(models.Model):
    id_compagnie = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class Aeroport(models.Model):
    id_aeroport = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=100)
    id_ville = models.ForeignKey(Ville, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Vol(models.Model):
    id_vol = models.AutoField(primary_key=True)
    date_depart = models.DateTimeField(default=datetime.now)
    date_arrive = models.DateTimeField(default=datetime.now)
    aeroport_depart = models.ForeignKey(Aeroport, on_delete=models.CASCADE, related_name='aeroport_depart')
    aeroport_arrivee = models.ForeignKey(Aeroport, on_delete=models.CASCADE, related_name='aeroport_arrivee')
    id_compagnie = models.ForeignKey(Compagnie, on_delete=models.CASCADE)
    montant = models.IntegerField( default= 0)

    def __str__(self):
        return f"Vol {self.id_vol}"
    
    
class FactureVol(models.Model):
    id_facture = models.AutoField(primary_key=True)
    montant = models.IntegerField()
    date_facture = models.DateField()

    def __str__(self):
        return f"Facture {self.id_facture}"


class ReservationVol(models.Model):
    num_reservation = models.AutoField(primary_key=True)
    date_reservation = models.DateField()
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_facture = models.ForeignKey(FactureVol, on_delete=models.CASCADE)
    id_vol = models.ForeignKey(Vol, on_delete=models.CASCADE)

    def __str__(self):
        return f"ReservationVol{self.num_reservation}"


class Escales(models.Model):
    heure_arrivee = models.DateTimeField()
    heure_depart = models.DateTimeField()
    id_aeroport = models.ForeignKey(Aeroport, on_delete=models.CASCADE)
    id_vol = models.ForeignKey(Vol, on_delete=models.CASCADE)

    def __str__(self):
        return f"Escale {self.id_aeroport} - {self.id_vol}"




class Societe(models.Model):
    id_societe = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    id_ville = models.ForeignKey(Ville, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class MarqueVoiture(models.Model):
    id_marque = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)

    def __str__(self):
        return self.nom


class ModeleVoiture(models.Model):
    id_modele = models.AutoField(primary_key=True)
    nom = models.CharField(max_length=50)
    id_marque = models.ForeignKey(MarqueVoiture, on_delete=models.CASCADE)

    def __str__(self):
        return self.nom


class Voiture(models.Model):
    vin = models.AutoField(primary_key=True)
    montant = models.IntegerField()
    id_modele = models.ForeignKey(ModeleVoiture, on_delete=models.CASCADE)
    id_societe=models.ForeignKey(Societe, on_delete=models.CASCADE)
    image=models.CharField(max_length=200)

    def __str__(self):
        return f"Voiture {self.vin}"


class FactureVoiture(models.Model):
    id_facture = models.AutoField(primary_key=True)
    montant = models.IntegerField()
    date_facture = models.DateField()

    def __str__(self):
        return f"Facture {self.id_facture}"


class ReservationVoiture(models.Model):
    num_reservation = models.AutoField(primary_key=True)
    date_reservation = models.DateField()
    date_retour = models.DateField()
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_facture = models.ForeignKey(FactureVoiture, on_delete=models.CASCADE)
    vin = models.ForeignKey(Voiture, on_delete=models.CASCADE)

    def __str__(self):
        return f"Réservation {self.num_reservation}"





