from tempfile import template

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'myfirstapp/index.html')

def main(request):
    return render(request,'myfirstapp/main.html')

def bonjour(request):
    nom = request.GET["nom"]
    return render(request,'myfirstapp/bonjour.html',{'nom':nom})
