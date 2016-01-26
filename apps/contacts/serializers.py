from rest_framework import serializers
from . import models


class OwnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Owner


class TenantSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tenant
