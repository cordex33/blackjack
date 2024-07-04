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
    g = Repartidor.objects.get(id=1)
    g.carta = '0'
    g.puntaje = '0'
    g.save()

    r = Jugador.objects.get(nombre=nombre)
    r.puntaje = '0'
    r.carta = '0'
    r.save()
    
    if request.method == 'GET' or request.POST.get('accion') == 'volver_jugar':

        repartidor = random.choice(cartas)
        jugador = random.choice(cartas)
        # Condición de repartidor
        if repartidor in ['J', 'Q', 'K', 'A']:
            guardar_repartidor = Repartidor.objects.get(nombre='XabalDelOcho')
            guardar_repartidor.carta = 10
            guardar_repartidor.puntaje = guardar_repartidor.carta + guardar_repartidor.puntaje
            guardar_repartidor.save()
        else:
            guardar_repartidor = Repartidor.objects.get(nombre='XabalDelOcho')
            #Guarda en la instancia .carta el valor de jugador (en letra)
            guardar_repartidor.carta = int(repartidor)
            guardar_repartidor.puntaje = guardar_repartidor.carta + guardar_repartidor.puntaje 
            guardar_repartidor.save()

        # Condición de jugar
        if jugador in ['J', 'Q', 'K', 'A']:
            nueva_carta = Jugador.objects.get(nombre=nombre)
            #Guarda en la instancia .carta el valor de jugador (en número)
            nueva_carta.carta = 10
            nueva_carta.puntaje = nueva_carta.carta + nueva_carta.puntaje 
            nueva_carta.save()
        
        else:
            nueva_carta = Jugador.objects.get(nombre=nombre)
            #Guarda en la instancia .carta el valor de jugador (en letra)
            nueva_carta.carta = int(jugador)
            nueva_carta.puntaje = nueva_carta.carta + nueva_carta.puntaje 
            nueva_carta.save()

    return render(request, 'pagina_jugar/jugar.html', {
        'nombre': nombre,
        'carta_jugador': Jugador.objects.get(nombre=nombre).carta,
        'total_jugador': Jugador.objects.get(nombre=nombre).puntaje,
        'repartidor': Repartidor.objects.get(id=1).carta,
        'total_repartidor': Repartidor.objects.get(id=1).puntaje,
    })

def pedir(request, nombre):
    if request.method == 'POST':
        accion = request.POST.get('accion')
        if accion == 'pedir':

            jugador = random.choice(cartas)
            if jugador in ['J', 'Q', 'K', 'A']:
                nueva_carta = Jugador.objects.get(nombre=nombre)
                #Guarda en la instancia .carta el valor de jugador (en número)
                nueva_carta.carta = 10
                nueva_carta.puntaje = nueva_carta.carta + nueva_carta.puntaje 
                nueva_carta.save()

            else:
                nueva_carta = Jugador.objects.get(nombre=nombre)
                #Guarda en la instancia .carta el valor de jugador (en letra)
                nueva_carta.carta = int(jugador)
                nueva_carta.puntaje = nueva_carta.carta + nueva_carta.puntaje 
                nueva_carta.save()
    
    return render(request, 'pagina_jugar/jugar.html', {
        'nombre': nombre,
        'carta_jugador': Jugador.objects.get(nombre=nombre).carta,
        'total_jugador': Jugador.objects.get(nombre=nombre).puntaje,
        'repartidor': Repartidor.objects.get(id=1).carta,
        'total_repartidor': Repartidor.objects.get(id=1).puntaje,
    })

def mantener(request, nombre):
    if request.method == 'POST':
        accion = request.POST.get('accion')
        if accion == 'mantener':
            repartidor = random.choice(cartas)

            if repartidor in ['J', 'Q', 'K', 'A']:
                nueva_carta = Repartidor.objects.get(id=1)
                nueva_carta.carta = 10
                nueva_carta.puntaje = nueva_carta.carta + nueva_carta.puntaje
                nueva_carta.save()
            
            else:
                nueva_carta = Repartidor.objects.get(id=1)
                nueva_carta.carta = int(repartidor)
                nueva_carta.puntaje = nueva_carta.carta + nueva_carta.puntaje
                nueva_carta.save()
    
    return render(request, 'pagina_jugar/jugar.html', {
        'nombre': nombre,
        'carta_jugador': Jugador.objects.get(nombre=nombre).carta,
        'total_jugador': Jugador.objects.get(nombre=nombre).puntaje,
        'repartidor': Repartidor.objects.get(id=1).carta,
        'total_repartidor': Repartidor.objects.get(id=1).puntaje,

    })
                

