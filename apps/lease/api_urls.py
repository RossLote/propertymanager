from rest_framework.routers import DefaultRouter
from . import api

router = DefaultRouter()
router.register(r'leases', api.LeaseViewset)

urlpatterns = router.urls
