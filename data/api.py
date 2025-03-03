import csv
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class DataViewSet(viewsets.ViewSet):
    
    @action(detail=False, methods=['get'], url_path='', url_name='data-root') 
    def all_value(self, request):
        file_path = './csv/science-and-technology-indicators-for-india-1.csv'
        
        try:
            with open(file_path, 'r', encoding="utf-8") as file:
                reader = csv.DictReader(file)
                Value = [row['Value'] for row in reader if 'Value' in row]
                
                if Value:
                    return Response({'Value': Value})
                else:
                    return Response({'error': 'Columna no encontrada'}, status=404)
        
        except FileNotFoundError:
            return Response({'error': 'Archivo no encontrado'}, status=404)