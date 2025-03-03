from rest_framework import routers
from .api import ProjectViewSet
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
#router.register('api/camila', camilaViewSet, 'camila')

urlpatterns = router.urls