from rest_framework import routers
from django.urls import path
from .api import ProjectViewSet, ApiDataCristianViewSet, ApiDataAndresViewSet, ApiDataCamilaViewSet
from .api_compas import ConsumoApiCristianView, ConsumoApiAndresView, ConsumoApiCamilaView
from users.api import UserViewSet
from data.api import DataViewSet
from agroandfarming.api import AgroAndFarmingViewSet
from evacolombia.api import EVAColombiaViewSet

#from apiandres.api import ApiAndresViewSet

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')
router.register('api/users', UserViewSet, 'users')
router.register('api/data', DataViewSet, 'data')
router.register('api/agroandfarming', AgroAndFarmingViewSet, 'agroandfarming')
router.register('api/evacolombia', EVAColombiaViewSet, 'evacolombia')
router.register('api/productos_cristian', ApiDataCristianViewSet, 'api_data_cristian')
router.register('api/projects_andres', ApiDataAndresViewSet, 'api_data_andres')
router.register('api/projects_camila', ApiDataCamilaViewSet, 'api_data_camila')

urlpatterns = router.urls

# Agregar la nueva vista de ConsumoApiView a las URLs
urlpatterns += [
    path('api/consumo1/', ConsumoApiCristianView.as_view(), name='api_data_cristian'),
    path('api/consumo2/', ConsumoApiAndresView.as_view(), name='api_data_andres'),
    path('api/consumo3/', ConsumoApiCamilaView.as_view(), name='api_data_camila'),
]
