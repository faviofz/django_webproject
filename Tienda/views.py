from django.shortcuts import render
from Tienda.models import Categoria, Producto

# Create your views here.


def tienda(request):
    categorias = Categoria.objects.all()
    productos = Producto.objects.all()
    return render(request, "tienda/tienda.html", {"productos": productos, "categorias":categorias})
