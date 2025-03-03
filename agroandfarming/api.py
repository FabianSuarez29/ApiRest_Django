import csv
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class AgroAndFarmingViewSet(viewsets.ViewSet):
    
    @action(detail=False, methods=['get'], url_path='', url_name='agroandfarming-root') 
    def Agro_and_Farming(self, request):
        file_path = './csv/agriculture_dataset.csv'
        
        try:
            with open(file_path, 'r', encoding="utf-8") as file:
                reader = csv.DictReader(file)
                agroandfarming = [row for row in reader]
                
                if agroandfarming:
                    return Response({'agroandfarming': agroandfarming})
                else:
                    return Response({'error': 'Archivo CSV vacío o sin datos válidos'}, status=404)
        
        except FileNotFoundError:
            return Response({'error': 'Archivo no encontrado'}, status=404)