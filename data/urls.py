from rest_framework import routers
from .api import DataViewSet

router = routers.DefaultRouter()

router.register('api/data.all_value', DataViewSet, 'data')

urlpatterns = router.urls