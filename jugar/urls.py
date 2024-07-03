from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('jugar/<str:nombre>', views.jugar, name="jugar"),
    path('crear_jugador/', views.crear_jugador, name="crear_jugador"),
]