from django.ulrs import path,include
from . import views
from ..firstproject.urls import urlpatterns

urlpatterns = [
    path (route:'index/', views.index),
]