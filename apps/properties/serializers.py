from rest_framework import serializers
from . import models


class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Property

                
class TenancySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tenancy
