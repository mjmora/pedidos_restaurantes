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

#from .forms import PostForm

from manejo_pedidos.models import *
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
	nombre=request.POST.get('name')
	mail=request.POST.get('email')
	cd=request.POST.get('cedula')
	telefono=request.POST.get('numero')
	direc=request.POST.get('direccion')
	print (cd)
	cliente=Persona(nombre_persona=nombre,identificacion=cd,telefono=telefono,direccion=direc,mail=mail)
	cliente.save()

	client={'id':cd,'mesa':1}
	return render(request, 'menu.html',client,
		context_instance = RequestContext(request))


def cocina(request):
	pedido = Consumo.objects.filter(estado=False)
	return render(request, 'cocina.html',
		context_instance = RequestContext(request))


def reg_cliente(request):
	if request.method == "POST":
		form = PersonaForm(request.POST)
		print()
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			print(post)
	        return redirect('index')
	else:
		form = PersonaForm()
	return render(request, 'cliente.html', {'form': form})


