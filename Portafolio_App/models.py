from django.db import models

# Create your models here.
class PortafolioProjects(models.Model):
    nombre = models.CharField(max_length=255, help_text='Nombre del proyecto')
    descripcion = models.CharField(max_length=255)
    tecologias = models.JSONField(help_text='Tecnologías del proyecto')
    github_link = models.URLField(max_length=255, help_text='Link de Github')
    imagen = models.ImageField(upload_to='images', blank=True)

    def __str__(self):
        return self.nombre
