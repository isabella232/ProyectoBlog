from django.db import models
from ckeditor.fields import RichTextField
#Importado modelo de usuario nativo de django
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Nombre")
    description = models.CharField(max_length=255, verbose_name="Descripción")
    created_at = models.DateField(auto_now_add=True, verbose_name="Creado el ")

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Categoría"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name="Titulo")
    content = RichTextField(verbose_name="Contenido")
    image = models.ImageField(default="null", verbose_name="Imagen", upload_to = 'articles')
    public = models.BooleanField(verbose_name="¿Publicado?")
    user = models.ForeignKey(User, verbose_name="Usuario", editable=False ,on_delete=models.CASCADE) #Me guarda el ide del usuario del articulo en la base de datos
    categories = models.ManyToManyField(Category, verbose_name="Categorias", blank=True, related_name="articles")#Muchos articulos pueden tener muchas categorias, me guarda las relaciones que hay entre un articulo y una categoria en la base de datos 
    created_at = models.DateField(auto_now_add=True, verbose_name="Creado el ")
    update_at = models.DateField(auto_now=True, verbose_name="Editado el ")

    class Meta:
        verbose_name = "Articulo"
        verbose_name_plural = "Articulos"

    def __str__(self):
        return self.title