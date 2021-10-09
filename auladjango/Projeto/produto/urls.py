from django.urls import path
from . import views # forma de importar da própria pasta

urlpatterns = [
    path('', views.metodo)
]