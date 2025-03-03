import csv
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

class EVAColombiaViewSet(viewsets.ViewSet):
    
    @action(detail=False, methods=['get'], url_path='', url_name='evacolombia-root') 
    def all_evacolombia(self, request):
        file_path = './csv/Evaluaciones_Agropecuarias_Municipales_EVA.csv'
        
        try:
            with open(file_path, 'r') as file:
                reader = csv.DictReader(file)
                evacolombia = [row for row in reader]
                
                if evacolombia:
                    return Response({'evacolombia': evacolombia})
                else:
                    return Response({'error': 'Archivo CSV vacío o sin datos válidos'}, status=404)
        
        except FileNotFoundError:
            return Response({'error': 'Archivo no encontrado'}, status=404)