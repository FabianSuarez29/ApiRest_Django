import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import models
from .models import ApiDataCristian, ApiDataAndres, ApiDataCamila

class ConsumoApiCristianView(APIView):
    def get(self, request, *args, **kwargs):
        # URL del endpoint de la API externa
        url = 'http://3.19.235.79:8000/api/productos/'
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Para lanzar un error si el código de estado no es 2xx
        except requests.exceptions.HTTPError as errh:
            return Response({'error': f'HTTP Error: {errh}'}, status=status.HTTP_400_BAD_REQUEST)
        except requests.exceptions.RequestException as err:
            return Response({'error': f'Request Error: {err}'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Parseamos los datos JSON recibidos
        data = response.json()

        # Guardamos los datos en la base de datos
        for item in data:
            # Verificamos si ya existe el registro en la base de datos por el `api_id`
            obj, created = ApiDataCristian.objects.update_or_create(
                id=item['id'],
                defaults={
                    'descripcion': item.get('descripcion'),
                    'stock': item.get('stock'),
                    'ubicacion': item.get('ubicacion'),
                }
            )

        return Response({"message": "Datos almacenados correctamente"}, status=status.HTTP_201_CREATED)
    
class ConsumoApiAndresView(APIView):
    def get(self, request, *args, **kwargs):
        # URL del endpoint de la API externa
        url = 'http://3.131.123.55:8000/api/projects/'
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Para lanzar un error si el código de estado no es 2xx
        except requests.exceptions.HTTPError as errh:
            return Response({'error': f'HTTP Error: {errh}'}, status=status.HTTP_400_BAD_REQUEST)
        except requests.exceptions.RequestException as err:
            return Response({'error': f'Request Error: {err}'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Parseamos los datos JSON recibidos
        data = response.json()

        # Guardamos los datos en la base de datos
        for item in data:
            # Verificamos si ya existe el registro en la base de datos por el `api_id`
            obj, created = ApiDataAndres.objects.update_or_create(
                id=item['id'],
                defaults={
                    'title': item.get('title'),
                    'description': item.get('description'),
                    'technology': item.get('technology'),
                }
            )

        return Response({"message": "Datos almacenados correctamente"}, status=status.HTTP_201_CREATED)
    
class ConsumoApiCamilaView(APIView):
    def get(self, request, *args, **kwargs):
        # URL del endpoint de la API externa
        url = 'http://18.223.195.38:8000/api/projects/'
        
        try:
            response = requests.get(url)
            response.raise_for_status()  # Para lanzar un error si el código de estado no es 2xx
        except requests.exceptions.HTTPError as errh:
            return Response({'error': f'HTTP Error: {errh}'}, status=status.HTTP_400_BAD_REQUEST)
        except requests.exceptions.RequestException as err:
            return Response({'error': f'Request Error: {err}'}, status=status.HTTP_400_BAD_REQUEST)
        
        # Parseamos los datos JSON recibidos
        data = response.json()

        # Guardamos los datos en la base de datos
        for item in data:
            # Verificamos si ya existe el registro en la base de datos por el `api_id`
            obj, created = ApiDataCamila.objects.update_or_create(
                id=item['id'],
                defaults={
                    'title': item.get('title'),
                    'description': item.get('description'),
                    'technology': item.get('technology'),
                }
            )

        return Response({"message": "Datos almacenados correctamente"}, status=status.HTTP_201_CREATED)
    