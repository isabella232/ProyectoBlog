from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm #Cargamos la case que contiene los campos del formulario
from .forms import RegisterForm #CARGAMOS DE form.py el formulario que hemos creado
from django.contrib import messages #importamos para mostrar mensajes flash e la pantalla
from django.contrib.auth import authenticate, login, logout #cargamos los modulos que necesitamos para autenticar el usuario, iniciar sesión y cerrar sesión
from django.contrib.auth.decorators import login_required #importamos decorador para restringir acceso a la página de mi web y que sean accesibles solo si se ha iniciado sesión


# Create your views here.

def index(request):
    return render(request, 'mainapp/index.html', {
        'title': 'Inicio'
    })


def about(request):
    return render(request, 'mainapp/about.html', {
        'title': 'Sobre nosotros'
    })


def register_page(request):

    if request.user.is_authenticated:
        return redirect('inicio')

    else:
        register_form = RegisterForm()

        if request.method == 'POST':
            register_form = RegisterForm(request.POST)

            if register_form.is_valid():
                register_form.save()
                messages.success(request, 'Te has registrado correctamente')

                return redirect("inicio")

        return render(request, "users/register.html", {
            'title': 'Registro',
            'register_form': register_form
        })

def login_page(request):

    if request.user.is_authenticated:
        return redirect('inicio')

    else:

        if request.method == 'POST':
            username = request.POST.get("username") #recogemos el nombre de usuario
            password = request.POST.get("password") #recogemos la contraseña

            user = authenticate(request, username=username, password=password)

            if user is not None: #Verificamos que el user no sea none
                login(request, user) #si el user no es none hacemos el login
                return redirect('inicio') #redireccionamos a inicio

            else:
                messages.warning(request, 'No te has identificado correctamente') #si el usuario es none le indicamos que no se ha logueado correctamente

        return render(request, 'users/login.html', {
            'title': 'Identificate'
        })


def logout_user(request):
    logout(request)

    return redirect('login')