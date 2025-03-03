from rest_framework import serializers
from .models import Project
from .models import ApiDataCristian, ApiDataAndres, ApiDataCamila

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description', 'technology', 'created_at')
        read_only_fields = ('created_at', )
        
class ApiDataCristianSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiDataCristian
        fields = ['id', 'descripcion', 'stock', 'ubicacion']
              
class ApiDataAndresSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiDataAndres
        fields = ['id', 'title', 'description', 'technology']        
        
class ApiDataCamilaSerializer(serializers.ModelSerializer):
    class Meta:
        model = ApiDataCamila
        fields = ['id', 'title', 'description', 'technology'] 
        