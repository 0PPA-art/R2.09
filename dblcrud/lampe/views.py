from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from . forms import CategorieForm
from . forms import ProduitForm
from . import models


def ajout(request, type_objet):
    if type_objet == 'produit':
        formp = ProduitForm(request.POST or None)
        if request.method == "POST" and formp.is_valid():
            formp.save()  # ← manquant !
            return HttpResponseRedirect(reverse('lampe:affiche'))
        return render(request, "lampe/ajout_categorie.html", {"form": formp})

    elif type_objet == 'categorie':
        formc = CategorieForm(request.POST or None)
        if request.method == "POST" and formc.is_valid():
            formc.save()
            return HttpResponseRedirect(reverse('lampe:affiche'))
        return render(request, "lampe/ajout_categorie.html", {"form": formc})


def traitement(request):
    lform = ProduitForm(request.POST)
    if lform.is_valid():
        livre = lform.save()
        return render(request,"lampe/affiche.html",{"bibliothequeapp" : livre})
    else:
        return render(request,"lampe/ajout_categorie.html",{"form": lform})

def affiche(request):
    categories = models.Categorie.objects.all()
    produits = models.Produit.objects.all()
    return render(request, "lampe/affiche.html", {
        "categories": categories,
        "produits": produits
    })
def traitementupdate(request, id):
    Livre = models.Produit.objects.get(pk=id)  # méthode pour récupérer les donnéesdans la base avec un id donnée
    lform = ProduitForm(request.POST)
    if lform.is_valid():
        Livre = lform.save(commit=False) # création d'un objet bibliothequeapp avec les données duformulaire mais sans l'enregistrer dans la base.
        Livre.id = id # modification de l'id de l'objet
        Livre.save() # mise à jour dans la base puisque l'id du bibliothequeapp existe déja.
        return HttpResponseRedirect("/lampe/") # plutot que d'avoir un gabarit
#pour nous indiquer que cela c'est bien passé, nous repartons sur une autre action
#qui renvoie vers la page d'index de notre site (celle avec la liste des entrées)
    else:
        return render(request, "lampe/update.html", {"form": lform, "id": id})
def liste(request, type_objet):
    if type_objet == 'categorie':
        objets = models.Categorie.objects.all()
        template = "lampe/liste_categorie.html"
        titre = "Liste des catégories"

    elif type_objet == 'produit':
        objets = models.Produit.objects.all()
        template = "lampe/liste_produit.html"
        titre = "Liste des produits"

    return render(request, template, {
        "objets": objets,
        "titre": titre
    })

def update(request, id):
    Livre = models.Produit.objects.get(pk=id)
    form = ProduitForm(Livre.__dict__)  # création d'un formulaire vide
    return render(request, "lampe/update.html", {"form": form, "id":id})

def delete(request, id):
    livre = models.Produit.objects.get(pk=id)
    livre.delete()
    return HttpResponseRedirect('/lampe/liste/')


