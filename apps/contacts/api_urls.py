from rest_framework.routers import DefaultRouter
from . import api

router = DefaultRouter()
router.register(r'owners', api.OwnerViewset)
router.register(r'tenants', api.TenantViewset)

urlpatterns = router.urls
