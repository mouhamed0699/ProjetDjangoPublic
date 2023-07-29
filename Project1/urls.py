"""
URL configuration for Project1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.contrib import admin
from django.urls import path
from AppliDjango.views import Profil, chambres, connexion, deconnexion, deconnexionChambre, index, inscription, rechercher_chambre, rechercher_voiture, rechercher_vol, reservationChambre, reservationVoiture, voiture, vol,login_view
urlpatterns = [
    path("", index, name="index"),
    path('voiture/', voiture, name='voiture'),
    path('chambres/', chambres, name='chambres'),
    path('vol/', vol, name='vol'),
    path('connexion/', connexion, name='connexion'),
    path('inscription/', inscription, name='inscription'),
    path('rechercher_chambre/', rechercher_chambre, name='rechercher_chambre'),
    path('rechercher_voiture/', rechercher_voiture, name='rechercher_voiture'),
    path('reservationChambre/', reservationChambre, name='reservationChambre'),
    path('reservationVoiture/', reservationVoiture, name='reservationVoiture'),
    path('rechercher_vol/', rechercher_vol, name='rechercher_vol'),
    path('deconnexion/', deconnexion, name='deconnexion'),
    path('Profil/', Profil, name='Profil'),
    path('deconnexionChambre/', deconnexionChambre, name='deconnexionChambre'),
    path("admin/", admin.site.urls),
]
