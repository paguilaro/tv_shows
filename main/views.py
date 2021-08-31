import bcrypt
from django.shortcuts import render, HttpResponse, redirect
from .models import Show, Network, Users
from django.contrib import messages
from django.db import IntegrityError 
from .decorators import login_protect

@login_protect
def index(request):
    shows=Show.objects.all()
    context = {
        'saludo': 'Hola',
        "shows":shows
    }
    return render(request, 'index.html', context)

# shows/new
@login_protect
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
@login_protect
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
        # después editamos el Show
        target_show=Show.objects.get(id=show_id)
        target_show.title=title
        target_show.network_id=network_id
        target_show.release_date=release_date
        target_show.description=description
        target_show.save()

        #Show.objects.create(title=title, network_id=network_id, release_date=release_date, description=description)
        # Finalmente devolvemos al usuario a la pantalla de los shows
        return redirect('/shows ') 
    #post actualiza los datos
    #if request.method=="POST":
    #title = request.POST['title']

@login_protect
def detalle(request, show_id):
    s=Show.objects.get(id=show_id)

    context = {
        'show': s
    }
    return render(request, 'detalle.html', context)

@login_protect
def delete(request, show_id):
    #lo vamos a buscar
    s=Show.objects.get(id=show_id)
    #lo vamos a borramos 
    s.delete()

    #redirigir 
    return redirect('/shows')


def register(request):
    #si llega por el GET muestro el template
    if request.method == 'GET':
        return render(request, 'register.html')

    else:
        #si llega por un POST, tomar valores del formulario
        #y crear un nuevo usuario
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        #validar que el formulario este correcto
        errors = Users.objects.basic_validator(request.POST)
        if len(errors) > 0:
            #en este caso, hay al menos 1 error en el formulario
            #voy a mostrarle los errores al usuario
            for llave, mensaje_de_error in errors.items():
                messages.error(request, mensaje_de_error)

            return redirect('/register')

    #Incluir en import linea 2 de este archivo (views.py)
    #Si llego aca, las contrasenas coinciden 
    #e inicia registro en base de datos con el nombre user
    try:
        user = Users.objects.create(
            #pasamos los parametros del request.POST
            name=name,
            email=email,
            password=bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        )
        
        #se necesita guardar en sesion en un diccionario c/datos de usuario
        request.session['user']= {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'avatar': user.avatar
        }
        messages.success(request, 'Usuario creado con exito')
        return redirect('/shows')
    except IntegrityError:
        messages.error(request, 'Usuario ya existe')
        return redirect('/register')

    #y se reenvia a pagina principal landing
    

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    try:
        user= Users.objects.get(email=email) 
    except Users.DoesNotExist:
        messages.error(request, 'Usuario inexistente o contrasena incorrecta')
        return redirect('/register')

    #si entramos aca, estamos seguros que al menos el usuario existe
    if  not bcrypt.checkpw(password.encode(), user.password.encode()):
        messages.error(request, 'Usuario inexistente o contrasena incorrecta')
        return redirect('/register')

    #si entra por este request, el usuario y la contrasena esta correcta, y entra a sesion
    request.session['user']={
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'avatar': user.avatar
    }
    messages.success(request, f'Hola {user.name}')
    return redirect('/shows') 

def logout(request):
    #request.session.clear()
    del request.session['user'] 
    return redirect('/register')
