from django.shortcuts import render
from .models import Category, Photo

# Create your views here.

def gallery(request):
    categorias = Category.objects.all()
    fotos = Photo.objects.all()

    context = {
        'categorias': categorias,
        'fotos': fotos,
    }

    return render (request, 'photos/gallery.html', context)

def wiewPhoto(request, pk):
    foto = Photo.objects.get(id=pk)
    context = {
        'foto': foto,
    }

    return render (request, 'photos/photo.html', context)

def addPhoto(request):
    return render (request, 'photos/add.html')