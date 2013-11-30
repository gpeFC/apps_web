# Administrador de la Aplicacion.

from principal.models import Pyme, Comentario
from django.contrib import admin

admin.site.register(Pyme)
admin.site.register(Comentario)
