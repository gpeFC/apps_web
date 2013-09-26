# Vista_Recetario

from django.shortcuts import render_to_response
from django.http import HttpResponse


def sobre(request):
	html = "<html><body>Proyecto de ejemplo en MDW</body></html>"
	return HttpResponse(html)