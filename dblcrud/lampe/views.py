from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from . forms import CategorieForm
from . forms import ProduitForm
from . import models


def ajout(request):
    if request.method == "POST": # arrive en cas de retour sur cette page après unesaisie invalide on récupère donc les données. Normalement nous ne devrions pas passer par ce chemin la pour le traitement des données
        form = ProduitForm(request)
        if form.is_valid(): # validation du formulaire.
            Livre = form.save() # sauvegarde dans la base
            return render(request,"lampe/affiche.html",{"bibliothequeapp" : Livre}) #envoie vers une page d'affichage du bibliothequeapp créé
        else:
            return render(request,"lampe/ajout.html",{"form": form})
    else :
        form = ProduitForm() # création d'un formulaire vide
        return render(request,"lampe/ajout.html",{"form" : form})

def traitement(request):
    lform = ProduitForm(request.POST)
    if lform.is_valid():
        livre = lform.save()
        return render(request,"lampe/affiche.html",{"bibliothequeapp" : livre})
    else:
        return render(request,"lampe/ajout.html",{"form": lform})

def read(request, id):
    Livre = models.Produit.objects.get(pk=id) # méthode pour récupérer les données dans la base avec un id donnée
    return render(request,"lampe/affiche.html",{"bibliothequeapp": Livre})

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
def liste(request):
    livres = models.Produit.objects.all()          # Pas besoin de list()
    return render(request, "lampe/liste.html", {
        "livres": livres
    })

def update(request, id):
    Livre = models.Produit.objects.get(pk=id)
    form = ProduitForm(Livre.__dict__)  # création d'un formulaire vide
    return render(request, "lampe/update.html", {"form": form, "id":id})

def delete(request, id):
    livre = models.Produit.objects.get(pk=id)

    livre.delete()
    return HttpResponseRedirect('/lampe/liste/')

