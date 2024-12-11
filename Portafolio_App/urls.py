from django.urls import path
from .views import PortafolioMethods

urlpatterns = [
    path('projects', PortafolioMethods.get_projects, name='projects'),
]