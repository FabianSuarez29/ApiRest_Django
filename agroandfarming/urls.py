from rest_framework import routers
from .api import AgroAndFarmingViewSet

router = routers.DefaultRouter()

router.register('api/agroandfarming', AgroAndFarmingViewSet, 'agroandfarming')

urlpatterns = router.urls