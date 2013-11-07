# Create your views here.

from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext


# Vista "Inicio".
def inicio(request):
    return render_to_response('inicio.html', context_instance=RequestContext(request))
