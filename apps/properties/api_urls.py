from rest_framework.routers import DefaultRouter
from . import api

router = DefaultRouter()
router.register(r'properties', api.PropertyViewset)
router.register(r'units', api.UnitViewset)

urlpatterns = router.urls
