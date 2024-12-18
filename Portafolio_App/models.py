from django.db import models
# Create your models here.

class tecnologies(models.Model):
    title = models.CharField(max_length=255, help_text='titulo de la tecnologia')
    disabled = models.BooleanField(default=False, help_text='si la tecnologia esta deshabilitada')
    href = models.URLField(max_length=255, help_text='link de la tecnologia')

    def __str__(self):
        return self.title

class statusProject(models.Model):
    title = models.CharField(max_length=255, help_text='titulo del estado')

    def __str__(self):
        return self.title

class PortafolioProjects(models.Model):
    name = models.CharField(max_length=255, help_text='Nombre del proyecto')
    description = models.CharField(max_length=255)
    github = models.URLField(max_length=255, help_text='Link de Github')
    vsCode = models.URLField(max_length=255, help_text='Link de VSCode')
    imagen = models.ImageField(upload_to='images/', blank=True, null=True)
    technologies = models.ManyToManyField(tecnologies, default=None)
    Estado = models.ManyToManyField(statusProject, default=None)
    date = models.DateField(auto_now=True, help_text='Fecha de creacion del proyecto')

    def __str__(self):
        return self.name


class PortafolioWorks(models.Model):
    cargo = models.CharField(max_length=255, help_text='Cargo del trabajo')
    empresa = models.CharField(max_length=255, help_text='Empresa del trabajo')
    descripcion = models.CharField(max_length=255, help_text='Descripcion del trabajo')
    inicio = models.CharField(max_length=255, help_text='Fecha de inicio del trabajo')
    fin = models.CharField(max_length=255, help_text='Fecha de fin del trabajo')
    tareas = models.JSONField(help_text='Tareas del trabajo', default=list)

    def __str__(self):
        return f'{self.cargo} -- {self.empresa}'