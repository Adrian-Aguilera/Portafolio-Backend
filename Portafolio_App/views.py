from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
# Create your views here.


class PortafolioMethods(APIView):
    @api_view(['GET'])
    @permission_classes([IsAuthenticated])
    def get_projects(request):
        return Response({'message': 'Portafolio_projects'})
