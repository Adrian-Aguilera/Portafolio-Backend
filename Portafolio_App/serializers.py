from rest_framework import serializers
from .models import PortafolioProjects, tecnologies, statusProject, PortafolioWorks

class tecnologiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = tecnologies
        fields = ['title', 'disabled', 'href']

class statusProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = statusProject
        fields = ['title']

class PortafolioProjectsSerializer(serializers.ModelSerializer):
    technologies = tecnologiesSerializer(many=True)
    Estado = statusProjectSerializer(many=True)
    class Meta:
        model = PortafolioProjects
        fields = ['name', 'description', 'github', 'vsCode', 'imagen', 'technologies', 'Estado', 'date']


class PortafolioWorksSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortafolioWorks
        fields = ['cargo', 'empresa', 'descripcion', 'inicio', 'fin', 'tareas']