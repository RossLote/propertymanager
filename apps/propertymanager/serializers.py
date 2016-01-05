from rest_framework import serializers
from . import models

class AddressSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Address
        
        
class LandlordSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Landlord
        
        
class PropertySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Property
        
        
class RoomSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Room
        
        
class TenantSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Tenancy
        
        
class TenancySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = models.Tenancy