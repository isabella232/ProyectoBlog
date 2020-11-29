from django.shortcuts import render
from .models import Page
from django.contrib.auth.decorators import login_required

# Create your views here.

#Función que nos saque una sola página de la base de datos

@login_required(login_url="login")
def page(request, slug):

    page = Page.objects.get(slug=slug)

    return render(request, "pages/page.html", {
        "page": page
    })