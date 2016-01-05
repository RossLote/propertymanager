from rest_framework import viewsets
from . import models, serializers


class TeamedObjectViewsetMixin(object):
    
    def get_queryset(self):
        
        return self.queryset.filter(
            team__users__user=self.request.user
        )

class AddressViewset(TeamedObjectViewsetMixin, viewsets.ModelViewSet):
    
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    

class LandlordViewset(TeamedObjectViewsetMixin, viewsets.ModelViewSet):
    
    queryset = models.Landlord.objects.all()
    serializer_class = serializers.LandlordSerializer
    

class PropertyViewset(TeamedObjectViewsetMixin, viewsets.ModelViewSet):
    
    queryset = models.Property.objects.all()
    serializer_class = serializers.PropertySerializer
    

class RoomViewset(TeamedObjectViewsetMixin, viewsets.ModelViewSet):
    
    queryset = models.Room.objects.all()
    serializer_class = serializers.RoomSerializer
    

class TenantViewset(TeamedObjectViewsetMixin, viewsets.ModelViewSet):
    
    queryset = models.Tenant.objects.all()
    serializer_class = serializers.TenantSerializer
    

class TenancyViewset(TeamedObjectViewsetMixin, viewsets.ModelViewSet):
    
    queryset = models.Tenancy.objects.all()
    serializer_class = serializers.TenancySerializer
    

class AddressViewset(TeamedObjectViewsetMixin, viewsets.ModelViewSet):
    
    queryset = models.Address.objects.all()
    serializer_class = serializers.AddressSerializer
    

