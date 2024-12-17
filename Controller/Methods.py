from Portafolio_App.models import PortafolioProjects
from Portafolio_App.serializers import PortafolioProjectsSerializer

class Methods:
    def get_projects():
        projects =  PortafolioProjects.objects.all()
        serializer = PortafolioProjectsSerializer(projects, many=True)
        return serializer.data