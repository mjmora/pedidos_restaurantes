from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

def index(request):
    return HttpResponse("Hello, world. You're at the Manejo pedidos  index.")

def escaneo(request):
	titulo ={'restaurante':"La Sazon de la Abuela"}
	return render(request, 'escaneo2.html',titulo,
		context_instance = RequestContext(request))

def prueba(request):
	titulo ={'restaurante':"Prueba escaneo"}
	return render(request, 'test.html',titulo,
		context_instance = RequestContext(request))

	