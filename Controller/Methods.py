from Portafolio_App.models import PortafolioProjects, PortafolioWorks
from Portafolio_App.serializers import PortafolioProjectsSerializer, PortafolioWorksSerializer

class Methods:
    def get_projects():
        projects =  PortafolioProjects.objects.all()
        serializer = PortafolioProjectsSerializer(projects, many=True)
        return serializer.data
    
    def get_works():
        works =  PortafolioWorks.objects.all()
        serializer = PortafolioWorksSerializer(works, many=True)
        return serializer.data