from django.contrib import admin
from .models import Article, Category

#Con estas clases lo que hacemos es mostrar la fecha en el panel de administración al momento de modificar las categorias y artículos
class CategoryAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',) #Ponemos una , para que interprete esto como un tupla
    list_display = ('name', 'created_at')
    search_fields = ('name', 'description')

class ArticleAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at', 'update_at', 'user')
    search_fields = ('title', 'content', 'user__username', 'categories__name') #user__username buscamos por nombre de usario con __ accedemos a una propiedad que hay dentro del modelo que está relacionado con el modelo de articulo
    list_display = ('title', 'user', 'created_at', 'public')
    list_filter = ('public', 'user__username', 'categories__name')#categories__name accedemos a una propiedad que hay dentro del modelo que está relacionado con el modelo de articulo

    #los parametros self, request, obj, form, change son parametros necesarios para poder crear un hook
    #lo que dice basicamenta la función es que si no hay un obj.user.id este va hacer igual al request.user.id que es el usuario que ha creado el articulo
    def save_model(self, request, obj, form, change):
        if not obj.user_id:
            obj.user_id = request.user.id
        
        obj.save()


# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article,ArticleAdmin)