from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import RequestContext
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.core import serializers

def index(request):
    return render(request, 'index.html',
		context_instance = RequestContext(request))

def escaneo(request):
	titulo ={'restaurante':"La Sazon de la Abuela"}
	return render(request, 'escaneo.html',titulo,
		context_instance = RequestContext(request))



	