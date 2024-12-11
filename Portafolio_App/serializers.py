from rest_framework import serializers
from .models import PortafolioProjects

class PortafolioProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PortafolioProjects
        fields = '__all__'