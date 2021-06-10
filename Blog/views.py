from django.http.response import HttpResponse
from django.shortcuts import render
from Blog.models import Categoria, Post
# Create your views here.


def blog(request):
    posts = Post.objects.all()
    return render(request, "blog/blog.html", {"posts":posts,})


def categoria(request, categoria_id):
    categoria = Categoria.objects.get(id=categoria_id)
    posts = Post.objects.filter(categorias=categoria.id)
    return render(request, "blog/categoria.html", {"categoria":categoria, "posts":posts})
