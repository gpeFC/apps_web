#encoding:utf-8
""" Archivo para formularios.  """

from django.forms import ModelForm
from django import forms
from principal.models import Pyme, Comentario

class PymeForm(ModelForm):
    class Meta:
        model = Pyme

class ComentarioForm(ModelForm):
    class Meta:
        model = Comentario


