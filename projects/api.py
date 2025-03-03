from .models import Project, ApiDataCristian, ApiDataAndres, ApiDataCamila
from .serializers import ProjectSerializer, ApiDataCristianSerializer, ApiDataAndresSerializer, ApiDataCamilaSerializer
from rest_framework import viewsets, permissions, status
from rest_framework.views import APIView
from rest_framework.response import Response

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer
    
class ApiDataCristianViewSet(viewsets.ModelViewSet):
    queryset = ApiDataCristian.objects.all()
    serializer_class = ApiDataCristianSerializer
    
class ApiDataAndresViewSet(viewsets.ModelViewSet):
    queryset = ApiDataAndres.objects.all()
    serializer_class = ApiDataAndresSerializer
    
class ApiDataCamilaViewSet(viewsets.ModelViewSet):
    queryset = ApiDataCamila.objects.all()
    serializer_class = ApiDataCamilaSerializer
    