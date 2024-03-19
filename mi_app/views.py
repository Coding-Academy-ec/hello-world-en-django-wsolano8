from django.shortcuts import render
from django.http import HttpResponse

def hello_world(request):
    return HttpResponse("¡Hola Mundo!")
# define una función llamada hello_world que utilice HttpResponse para devolver el mensaje ¡Hola Mundo!.
