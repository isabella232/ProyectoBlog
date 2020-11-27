from django.shortcuts import render
from .models import Page

# Create your views here.

#Función que nos saque una sola página de la base de datos

def page(request, slug):

    page = Page.objects.get(slug=slug)

    return render(request, "pages/page.html", {
        "page": page
    })