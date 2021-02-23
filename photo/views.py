from django.shortcuts import render, redirect
from .models import Category, Photo
import requests
import json
import cloudinary
import cloudinary.uploader
import cloudinary.api


# Create your views here.


def gallery(request):
    # es el dato que se pasa por el url
    category = request.GET.get('category')
    if category == None:
        fotos = Photo.objects.all()
    else:
        fotos = Photo.objects.filter(category__name=category)

    categorias = Category.objects.all()

    context = {
        'categorias': categorias,
        'fotos': fotos,
    }

    return render(request, 'photos/gallery.html', context)


def wiewPhoto(request, pk):
    foto = Photo.objects.get(id=pk)
    context = {
        'foto': foto,
    }

    return render(request, 'photos/photo.html', context)


def addPhoto(request):
    categorias = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        image = request.FILES.get('image')
        #print(image)
        

        # si la categoria seleccionada es diferente de none, osea cualquier otro menos none
        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        # si el campo de la nueva categoria tiene un string o algo
        elif data['category_new'] != '':
            # created es una variable extra que se pone true si la categoria en creada y false si no
            category, created = Category.objects.get_or_create(
                name=data['category_new'])
            print(created)
        # el default none a catoria si no selecciona y si no pone nada en nueva categoria
        else:
            category = None

        photo = Photo.objects.create(
            category=category,
            description=data['description'],
            image=image
        )
        lol = cloudinary.uploader.upload(photo.image)
        print(lol['secure_url'])

        return redirect('gallery')

    context = {
        'categorias': categorias,
    }

    return render(request, 'photos/add.html', context)
