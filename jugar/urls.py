from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('jugar/<str:nombre>', views.jugar, name="jugar"),
    path('crear_jugador/', views.crear_jugador, name="crear_jugador"),
    path('pedir/<str:nombre>', views.pedir, name='pedir'),
    path('mantener/<str:nombre>', views.mantener, name='mantener')
]