# Create your views here.

from principal.models import Pyme, Comentario
from principal.forms import PymeForm, ComentarioForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext


# Vista "Inicio".
def inicio(request):
    return render_to_response('inicio.html', context_instance=RequestContext(request))

# Vista "Contacto".
def contacto(request):
	return render_to_response('contacto.html', context_instance=RequestContext(request))

# Vista "Registro".
def registro(request):
	if request.method == 'POST':
		formulario = PymeForm(request.POST, request.FILES)
		if formulario.is_valid:
			formulario.save()
			return HttpResponseRedirect('/archivo')
	else:
		formulario = PymeForm()
	return render_to_response('registro.html', {'formulario':formulario}, context_instance=RequestContext(request))

# Vista "Acceder".
def acceder(request):
	return render_to_response('acceder.html', context_instance=RequestContext(request))

# Vista "Acerca de".
def acercade(request):
	return render_to_response('acercade.html', context_instance=RequestContext(request))

# Vista "Archivo".
def archivo(request):
	pymes = Pyme.objects.all()
	return render_to_response('archivo.html', {'pymes':pymes}, context_instance=RequestContext(request))


