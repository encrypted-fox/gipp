from rest_framework import routers
from .api import *


router = routers.DefaultRouter()

router.register('sites', SitesViewSet, 'sites'),
router.register('statuses', StatusesViewSet)
router.register('site_statuses', SiteStatusesViewSet)
router.register('html_heads', HtmlHeadsViewSet),
router.register('headers', HeadersViewSet),
router.register('footers', FootersViewSet),
router.register('mains', MainsViewSet),
router.register('added_blocks', AddedBlocksViewSet),
router.register('block_templates', BlockTemplatesViewSet),

urlpatterns = router.urls