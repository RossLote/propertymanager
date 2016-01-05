from rest_framework.routers import DefaultRouter
from . import api

router = DefaultRouter()
router.register(r'addresses', api.AddressViewset)
router.register(r'landlords', api.LandlordViewset)
router.register(r'properties', api.PropertyViewset)
router.register(r'rooms', api.RoomViewset)
router.register(r'tenants', api.TenantViewset)
router.register(r'tenancies', api.TenancyViewset)

urlpatterns = router.urls