from django.shortcuts import render, HttpResponse, redirect


def login_protect(func):
    def wrapper(request, *args , **kwargs):
        if 'user' not in request.session:
            return redirect('/register')
        respuesta=func(request,*args,**kwargs)
        return respuesta
    return wrapper
