from django.shortcuts import render
from django.http import HttpResponseRedirect
from . forms import LivreForm
from . import models
def ajout(request):
    if request.method == "POST": # arrive en cas de retour sur cette page après unesaisie invalide on récupère donc les données. Normalement nous ne devrions pas passer par ce chemin la pour le traitement des données
        form = LivreForm(request)
        if form.is_valid(): # validation du formulaire.
            Livre = form.save() # sauvegarde dans la base
            return render(request,"Livre/affiche.html",{"Livre" : Livre}) #envoie vers une page d'affichage du Livre créé
        else:
            return render(request,"Livre/ajout.html",{"form": form})
    else :
        form = LivreForm() # création d'un formulaire vide
        return render(request,"Livre/ajout.html",{"form" : form})

def traitement(request):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        Livre = lform.save()
        return render(request,"bibliothequeapp/affiche.html",{"Livre" : Livre})
    else:
        return render(request,"bibliothequeapp/ajout.html",{"form": lform})

def read(request, id):
    Livre = models.Livre.objects.get(pk=id) # méthode pour récupérer les donnéesdans la base avec un id donnée
    return render(request,"bibliothequeapp/affiche.html",{"Livre": Livre})

def traitementupdate(request, id):
    lform = LivreForm(request.POST)
    if lform.is_valid():
        Livre = lform.save(commit=False) # création d'un objet Livre avec les données duformulaire mais sans l'enregistrer dans la base.
        Livre.id = id # modification de l'id de l'objet
        Livre.save() # mise à jour dans la base puisque l'id du Livre existe déja.
        return HttpResponseRedirect("/bibliothequeapp/") # plutot que d'avoir un gabarit
#pour nous indiquer que cela c'est bien passé, nous repartons sur une autre action
#qui renvoie vers la page d'index de notre site (celle avec la liste des entrées)
    else:
        return render(request, "bibliothequeapp/update.html", {"form": lform, "id": id})


def update(request, id):
    lform = LivreForm(request.POST)
    livre = lform.save(commit=True)
    if request.method == "POST":
        form = LivreForm(request.POST, instance=livre)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/bibliothequeapp/')
    else:
        form = LivreForm(instance=livre)

    return render(request, "bibliothequeapp/update.html", {
        "form": form,
        "livre": livre,
        "id": id
    })