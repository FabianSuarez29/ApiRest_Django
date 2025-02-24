from rest_framework import routers
from .api import ProjectViewSet
from users.api import UserViewSet

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')
router.register('api/users', UserViewSet, 'users')

urlpatterns = router.urls