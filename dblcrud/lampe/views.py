from django.shortcuts import render

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from . forms import CategorieForm
from . forms import ProduitForm
from . import models


def ajout(request):
    if request.method == "POST":
        if type_objet == 'produit':
            formP = ProduitForm(request.POST, request.FILES)
            if formP.is_valid():
                formP.save()
                return HttpResponseRedirect('list')
            else:
                formC = CategorieForm()
        elif type_objet == 'categorie':
            formC = CategorieForm(request.POST)

            if formC.is_valid():
                formC.save()
                return HttpResponseRedirect('list')
            else:
                formC = CategorieForm()
        return render(request, "lampe/ajout.html", {"form": formC})


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

# ======= CRUD Catégorie ====================
def CategorieListView(ListView):
    model = Categorie
    template_name = 'lampe/liste.html'
    context_object_name = 'categories'

def CategorieCreateView(CreateView):
    model = Categorie
    form_class = CategorieForm
    template_name = ‘lampe/ajout.html'
    success_url = reverse_lazy('liste')


def CategorieUpdateView(UpdateView):
    model = Categorie
    form_class = CategorieForm
    template_name = 'lampe/update.html'
    success_url = reverse_lazy('liste ')

def CategorieDeleteView(DeleteView):
    model = Categorie
    template_name = ‘lampe/delete.html’
    success_url = reverse_lazy('liste')


# =============== CRUD Produit ==========
def ProduitListView(ListView):
    model = Produit
    template_name = ' lampe / liste.html'
    context_object_name = 'produits'


def ProduitCreateView(CreateView):
    model = Produit
    form_class = ProduitForm
    template_name = 'lampe/ajout.html'
    success_url = reverse_lazy('liste')


def ProduitUpdateView(UpdateView):
    model = Produit
    form_class = ProduitForm
    template_name = 'boutique/update.html'
    success_url = reverse_lazy('liste')


def ProduitDeleteView(DeleteView):
    model = Produit
    template_name = 'lampe / delete.html'
    success_url = reverse_lazy('liste ')
