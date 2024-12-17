from django.contrib import admin
from .models import PortafolioProjects, statusProject, tecnologies
# Register your models here.

admin.site.register(PortafolioProjects)
admin.site.register(statusProject)
admin.site.register(tecnologies)