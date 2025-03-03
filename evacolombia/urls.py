from rest_framework import routers
from .api import EVAColombiaViewSet

router = routers.DefaultRouter()

router.register('api/evacolombia', EVAColombiaViewSet, 'evacolombia')

urlpatterns = router.urls