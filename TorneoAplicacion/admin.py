from django.contrib import admin
from .models import productos

# Register your models here.
class productosAdmin(admin.ModelAdmin):
    list_display = ("codigoProducto", "descripcionProducto", "estatus")

admin.site.register(productos, productosAdmin)


from django.contrib import admin
from .models import Noticia

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'fecha_publicacion')  # Campos visibles en la lista de noticias
    search_fields = ('titulo',)  # Permitir búsquedas por título
    list_filter = ('fecha_publicacion',)  # Filtrar por fecha
    readonly_fields = ('fecha_publicacion',)  # Fecha solo lectura
    fields = ('titulo', 'contenido', 'imagen', 'fecha_publicacion')  # Campos visibles en el formulario

admin.site.register(Noticia, NoticiaAdmin)

from django.contrib import admin
from .models import Torneo, Inscripcion

class TorneoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin')  # Muestra estos campos en la lista
    search_fields = ('nombre',)  # Habilita la búsqueda por nombre de torneo
    list_filter = ('fecha_inicio',)  # Permite filtrar por fecha de inicio

class InscripcionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'torneo', 'fecha_inscripcion')
    search_fields = ('usuario__username', 'torneo__nombre')
    list_filter = ('torneo',)

admin.site.register(Torneo, TorneoAdmin)
admin.site.register(Inscripcion, InscripcionAdmin)
