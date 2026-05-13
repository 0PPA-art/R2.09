from django.contrib import admin

from django.contrib import admin
from .models import Categorie, Produit

@admin.register(Categorie)
class CategorieAdmin(admin.ModelAdmin):
    list_display = ['nom', 'description']

@admin.register(Produit)
class ProduitAdmin(admin.ModelAdmin):
    list_display = ['nom', 'categorie', 'prix', 'stock']
    list_filter = ['categorie']
    search_fields = ['nom']
