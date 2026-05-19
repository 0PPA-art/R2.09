from django.contrib import admin
from django.urls import path, include

from . import views

app_name = 'bibliothequeapp'   # ← Très important !

urlpatterns = [
    #Affichage
    path('', views.liste, name='liste'),
    path('traitement/', views.traitement),
    path('affiche/<int:id>/', views.read, name='read'),
    # Route pour afficher le formulaire de modification
    path('update/<int:id>/', views.update, name='update'),
    path('delete/<int:id>/', views.delete, name='delete'),# ← Doit être comme ça

    # Route pour traiter la modification (si tu veux garder 2 fonctions)
    path('traitementupdate/<int:id>/', views.traitementupdate, name='traitementupdate'),
    path('traitementupdate/<int:id>/', views.traitementupdate, name='traitementupdate'),
    # Catégories
    path('categories/', CategorieListView.as_view(), name='categorie_list'),
    path('categories/create/', CategorieCreateView.as_view(), name='categorie_create'),
    path('categories/<int:pk>/update/', CategorieUpdateView.as_view(), name='categorie_update'),
    path('categories/<int:pk>/delete/', CategorieDeleteView.as_view(), name='categorie_delete'),

    # Lampe
    path('produits/', ProduitListView.as_view(), name='produit_list'),
    path('produits/create/', ProduitCreateView.as_view(), name='produit_create'),
    path('produits/<int:pk>/update/', ProduitUpdateView.as_view(), name='produit_update'),
    path('produits/<int:pk>/delete/', ProduitDeleteView.as_view(), name='produit_delete'),

    path('ajout/categorie/', ajout, {'type_objet': 'categorie'}, name='ajout_categorie'),
    path('ajout/produit/', ajout, {'type_objet': 'produit'}, name='ajout_produit'),

    # Listes
    path('liste/categorie/', liste, {'type_objet': 'categorie'}, name='liste_categorie'),
    path('liste/produit/', liste, {'type_objet': 'produit'}, name='liste_produit'),
]