from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from Controller.Methods import Methods
# Create your views here.


class PortafolioMethods(APIView):
    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_projects(request):
        projects = Methods.get_projects()
        return Response({'data': projects})

    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def get_works(request):
        works = Methods.get_works()
        return Response({'data': works})

    @api_view(['GET'])
    #@permission_classes([IsAuthenticated])
    def activate_backend(request):
        return Response({'data': {
            'message': 'Backend is active'
        }})