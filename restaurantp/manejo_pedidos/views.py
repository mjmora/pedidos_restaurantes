from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
#from .forms import PostForm

from manejo_pedidos.models import *

def index(request):
	#nuevo = Mesa(numero=1,capacidad=4)
	#nuevo.save()
	return render(request, 'index.html',
		context_instance = RequestContext(request))

def escaneo(request):
	titulo ={'restaurante':"La Sazon de la Abuela"}
	return render(request, 'escaneo.html',titulo,
		context_instance = RequestContext(request))

def menu(request):
	nombre=request.POST.get('name')
	print nombre
	return render(request, 'menu.html',
		context_instance = RequestContext(request))

	
@csrf_exempt#decorador para que me permitta ingresar por un ajax y no por el navegador
def pedido_cliente(request):
    """
    """
    req = {}#crea un diccionario vacio
    if request.is_ajax() == True:
        nombre = request.POST['nombre']#hace referencia al valor enviado enel tmplate paralelo_buscador
        
        #obtiene los estudiantes cuyo id_paraleto es igual al id obtenido del templates donde su apellido sea igual a la letra
       
        req['mensaje'] = 'Correcto .... cargando datos '#para el diccionario crea una llave 
        return render(request, 'index.html',req,
		context_instance = RequestContext(request))

#def post_new(request):
	#from = PostForm()
#	if request.methos == "POST":
#		form=PostForm(request.POST)
#		if form.is_valid():
#			post = form.save(commit=False)
#	else:
#		form=PostForm()
#	return render(request,'',{'form':form})

	