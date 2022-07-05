from django.template import loader
from django.http import HttpResponse
from django.shortcuts import render

from .models import Publicacion

# Create your views here.

def inicio(request):
    return HttpResponse('hla')


def un_template(request):
    
    # template = loader.get_template('index.html')
    
    prueba1 = Publicacion(titulo = "Holamigente")
    prueba2 = Publicacion(titulo = "que tal")
    prueba3 = Publicacion(titulo = "que tal muchogusto")
     
    prueba1.save()
    prueba2.save()
    prueba3.save()
    
    # render = template.render({'lista_objetos': [prueba1, prueba2, prueba3]})
    
    # return HttpResponse(render)
    return render(request, 'index.html', {'lista_objetos': [prueba1, prueba2, prueba3]})

