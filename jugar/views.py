from django.shortcuts import render, redirect
from .forms import CrearJugador
from .models import Jugador, Repartidor
from .cartas import cartas
import random

# Create your views here.

def index(request):
    return render(request, 'index.html')


#Crea jugador y redirecciona a la página jugar y envía el nombre por link para saludarlo
def crear_jugador(request):
    if request.method == 'GET':
        return render(request, 'pagina_jugar/crear_jugador.html', {
            'form': CrearJugador()
        })
    else:
        Jugador.objects.create(nombre=request.POST['nombre'])
        return redirect('jugar', request.POST['nombre'])

#Página jugar que recibe un parametro, lo recibe de (crear_jugador)
def jugar(request, nombre):
    jugador = random.choice(cartas)
    repartidor = random.choice(cartas)

    #condición en caso que sea letra para cambiarlo a 10
    #-->falta que la 'A' cambie entre '1' y '10' dependiendo de la jugada.a
    
    if request.method == 'GET':
        if jugador in ['J', 'Q', 'K', 'A']:
            nueva_carta = Jugador.objects.get(nombre=nombre)
            nueva_carta.carta = int('10')
            #Guarda en el value 'puntaje' la carta anterior más la actual
            nueva_carta.puntaje = nueva_carta.carta + nueva_carta.puntaje 
            nueva_carta.save()
            
        else:
            nueva_carta = Jugador.objects.get(nombre=nombre)
            nueva_carta.carta = int(jugador)
            #Guarda en el value 'puntaje' la carta anterior más la actual
            nueva_carta.puntaje = nueva_carta.carta + nueva_carta.puntaje
            nueva_carta.save()
    
    #Detecta los botones de acción 'pedir' y 'mantener'
    elif request.method == 'POST':
        accion = request.POST.get('accion')
        if accion == 'pedir':
            if jugador in ['J', 'Q', 'K', 'A']:
                nueva_carta = Jugador.objects.get(nombre=nombre)
                nueva_carta.carta = int('10')
                #Guarda en el value 'puntaje' la carta anterior más la actual
                nueva_carta.puntaje = nueva_carta.carta + nueva_carta.puntaje 
                nueva_carta.save()
            else:
                nueva_carta = Jugador.objects.get(nombre=nombre)
                nueva_carta.carta = int(jugador)
                #Guarda en el value 'puntaje' la carta anterior más la actual
                nueva_carta.puntaje = nueva_carta.carta + nueva_carta.puntaje
                nueva_carta.save()
        
        elif accion == 'volver_jugar':
            nueva_carta = Jugador.objects.get(nombre=nombre)
            nueva_carta.carta = int('0')
            nueva_carta.puntaje = 0
            nueva_carta.save()

        elif accion == 'mantener':
            print("entro a mantener")
            #Obtenemos el nombre del repartidor
            nueva_carta_repartidor = Repartidor.objects.get(nombre='XabalDelOcho')
            #mientras sea abajo un número debajo del 17 se seguiran sacando cartas
            while nueva_carta_repartidor.puntaje < 17:
                
                print("entro al while")
                if repartidor in ['J', 'Q', 'K', 'A']:
                    nueva_carta_repartidor.carta = int('10')
                    
                    nueva_carta_repartidor.puntaje = nueva_carta_repartidor.carta + nueva_carta_repartidor.puntaje
                    nueva_carta_repartidor.save()
                else:
                    nueva_carta_repartidor.carta = int(repartidor)
                    nueva_carta_repartidor.puntaje = nueva_carta_repartidor.carta + nueva_carta_repartidor.puntaje
                    nueva_carta_repartidor.save()


    return render(request, 'pagina_jugar/jugar.html', {
        'nombre': nombre,
        'jugador': int(Jugador.objects.get(nombre=nombre).carta),
        'repartidor': repartidor,
        'puntaje': Jugador.objects.get(nombre=nombre).puntaje,
        'puntaje_repartidor': Repartidor.objects.get(nombre="XabalDelOcho").puntaje
    })

#Recibe si el jugador pide o mantiene sus cartas



