from django.contrib import admin
from.models import Page

#Configuración extra
class PageAdmin(admin.ModelAdmin):
    readonly_fields=('created_at', 'updated_at') #hacer que los campos que le he indicado sean solo de lectura
    search_fields = ('title', 'content')
    list_filter = ('visible',) #agregamos , para que interprete cómo tupla
    list_display = ('title', 'visible', 'created_at') #agregar columnas de información en el panel de administración
    ordering = ('created_at',)


# Register your models here.
admin.site.register(Page, PageAdmin)#Agregamos PageAdmin para que se apliquen los cambios en page

#Configuración de panel de administración
title = "Proyecto de Blog"
subtitle = "Panel de Gestión"

admin.site.site_header = title
admin.site.site_title = title
admin.site.index_title = subtitle