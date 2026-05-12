from django.urls import path
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('ajout/', views.ajout),
    path('traitement/', views.traitement),
    path('affiche/',views.read),
    path('update/',views.update, name='update'),
]