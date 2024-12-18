from django.contrib import admin
from .models import PortafolioProjects, statusProject, tecnologies, PortafolioWorks
# Register your models here.

admin.site.register(PortafolioProjects)
admin.site.register(statusProject)
admin.site.register(tecnologies)
admin.site.register(PortafolioWorks)