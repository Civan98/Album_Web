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
    categorias = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')

        print('data: ',data)
        print('image: ',image)

    context = {
        'categorias': categorias,
    }

    return render (request, 'photos/add.html', context)