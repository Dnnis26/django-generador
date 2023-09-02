from django.shortcuts import render
import random
from django.http import HttpResponse

# Create your views here.
def about(request):
    return render (request, 'about.html')

def inicio(request):
    return render(request, 'inicio.html')

def contraseña(request):
    characters = list("abcdefghijklmnñopqrstuvwxyz")
    contraseña_generada = ""
    
    length = int(request.GET.get('longitud'))
    
    if request.GET.get('mayusculas'):
        characters.extend(list('ABDCDEFGHIJKLMNÑOPQRSTUVWXYZ'))
    if request.GET.get('especial'):
        characters.extend(list('+-$%&=*'))
    if request.GET.get('numero'):
        characters.extend(list('1234567890'))
    
    for i in range(length):
        contraseña_generada += random.choice(characters)
        
    return render(request, 'contraseña.html', {'password': contraseña_generada} )

