from django import forms
from manejo_pedidos.models import *
from django.forms import ModelForm

class PersonaForm(forms.ModelForm):
	class Meta:
		model = Persona
		fields =  "__all__"
