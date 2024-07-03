from django import forms

class CrearJugador(forms.Form):
    nombre = forms.CharField(label="Nombre del jugador:", max_length=50)