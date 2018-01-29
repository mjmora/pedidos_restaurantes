from manejo_pedidos.models import *

from django.shortcuts import render
from django.forms import *
from forms import *
# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers
from django.utils import timezone
from django.shortcuts import redirect

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
	#nombre=request.GET.get['nombre']
	#print nombre
	return render(request, 'menu.html',
		context_instance = RequestContext(request))



def reg_cliente(request):
	if request.method == "POST":
		form = PersonaForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
	        return redirect('index')
	else:
		form = PersonaForm()
	return render(request, 'cliente.html', {'form': form})





# def pedido_cliente(request):
#     """
#     """
#     req = {}#crea un diccionario vacio
#     if request.is_ajax() == True:
#         nombre = request.POST['nombre']#hace referencia al valor enviado enel tmplate paralelo_buscador
#
#         req['mensaje'] = 'Correcto .... cargando datos '
#         return render(request, 'cliente.html',req,
# 		context_instance = RequestContext(request))
