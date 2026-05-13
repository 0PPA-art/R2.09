from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'bibliothequeapp'   # ← Très important !

urlpatterns = [
    path('', views.liste, name='liste'),
    path('ajout/', views.ajout),
    path('traitement/', views.traitement),
    path('affiche/<int:id>/', views.read, name='read'),
    # Route pour afficher le formulaire de modification
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),# ← Doit être comme ça

    # Route pour traiter la modification (si tu veux garder 2 fonctions)
    path('traitementupdate/<int:id>/', views.traitementupdate, name='traitementupdate'),
    path('traitementupdate/<int:id>/', views.traitementupdate, name='traitementupdate'),
                   # Page d'accueil de l'application
    path('liste/', views.liste, name='liste'),
]