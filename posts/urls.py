from rest_framework import routers
from .api import *


router = routers.DefaultRouter()

router.register('posts', PostsViewSet),

urlpatterns = router.urls