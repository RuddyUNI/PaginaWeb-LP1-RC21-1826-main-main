from django.db import models

# Create your models here.
class productos(models.Model):
    codigoProducto = models.IntegerField()
    descripcionProducto = models.CharField(max_length=255)
    estatus = models.BooleanField()

    def estatus_display(self):
        return "Disponible" if self.estatus else "No disponible"
    
from django.db import models

class Noticia(models.Model):
    titulo = models.CharField(max_length=200)  # Título de la noticia
    contenido = models.TextField()  # Contenido de la noticia
    fecha_publicacion = models.DateTimeField(auto_now_add=True)  # Fecha de creación (automática)
    imagen = models.ImageField(upload_to='noticias/', blank=True, null=True)  # Imagen opcional

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Noticia"
        verbose_name_plural = "Noticias"
        ordering = ['-fecha_publicacion']  # Las noticias más recientes primero

from django.db import models
from django.contrib.auth.models import User

class Torneo(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_fin = models.DateField()
    
    def __str__(self):
        return self.nombre

class Inscripcion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    torneo = models.ForeignKey(Torneo, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.usuario.username} inscrito en {self.torneo.nombre}'