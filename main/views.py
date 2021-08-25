from django.shortcuts import render, HttpResponse, redirect
from .models import Show, Network

def index(request):
    shows=Show.objects.all()
    context = {
        'saludo': 'Hola',
        "shows":shows
    }
    return render(request, 'index.html', context)

# shows/new
def new(request):
    #get : muestra el formulario con los datos del show para modificar
    if request.method=="GET":
        networks = Network.objects.all()
        context = {
            'saludo': 'Hola',
            "networks": networks
        }
        return render(request, 'new.html', context)
    #post inserta los datos nuevos
    if request.method=="POST":
        # primero recuperamos los valores del formulario
        title = request.POST['title']
        network_id = request.POST['network_id']
        release_date = request.POST['release_date']
        description= request.POST['description']
        # después creamos el nuevo Show
        Show.objects.create(title=title, network_id=network_id, release_date=release_date, description=description)
        # Finalmente devolvemos al usuario a la pantalla de los shows
        return redirect('/shows')

# shows/<show_id>/edit
def edit(request, show_id):
    #get : muestra el formulario con los datos del show para modificar
    if request.method=="GET":
        show=Show.objects.get(id=show_id)
        networks=Network.objects.all()

        release_date=show.release_date.strftime('%Y-%m-%d')

        context = {
            "show": show,
            "networks": networks,
            "release_date":release_date
        }
        return render(request, 'edit.html', context)

    #post inserta los datos nuevos
    if request.method=="POST":
        # primero recuperamos los valores del formulario
        title = request.POST['title']
        network_id = request.POST['network_id']
        release_date = request.POST['release_date']
        description= request.POST['description']
        # después creamos el nuevo Show
        Show.objects.create(title=title, network_id=network_id, release_date=release_date, description=description)
        # Finalmente devolvemos al usuario a la pantalla de los shows
        return redirect('/shows/<show_id>/edit') 
    #post actualiza los datos
    #if request.method=="POST":
    #title = request.POST['title']

def detalle(request, show_id):
    s=Show.objects.get(id=show_id)

    context = {
        'show': s
    }
    return render(request, 'detalle.html', context)

def delete(request, show_id):
    #lo vamos a buscar
    s=Show.objects.get(id=show_id)
    #lo vamos a borramos 
    s.delete()

    #redirigir 
    return redirect('/shows')