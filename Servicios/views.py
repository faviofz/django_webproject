from django.shortcuts import render
from Servicios.models import Servicio

# Create your views here.


def servicios(request):

    service = Servicio.objects.all()
    return render(request, "servicios/servicios.html", {"servicios": service})
