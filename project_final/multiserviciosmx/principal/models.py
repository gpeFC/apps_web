#encoding:utf-8
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

""" Modelo: Empresa. """
class Pyme(models.Model):
    usuario = models.ForeignKey(User)
    empresa = models.CharField(max_length=100, verbose_name="Empresa", unique=True)
    producto = models.CharField(max_length=100, verbose_name="Producto")
    descripcion = models.TextField(verbose_name="Descripcion", help_text="Descripcion del producto o servicio")
    logo = models.ImageField(upload_to="carga", verbose_name="Logotipo")
    foto = models.ImageField(upload_to="carga", verbose_name="Foto")


""" Modelo: Comentario. """
class Comentario(models.Model):
    alias = models.CharField(max_length=100, verbose_name="Alias")
    pyme = models.ForeignKey(Pyme)
    comentario = models.TextField(verbose_name="Comentario", help_text="Escribe tu comentario")

