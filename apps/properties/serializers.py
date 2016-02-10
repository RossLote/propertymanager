from rest_framework import serializers
from . import models


class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Property
        exclude = (
            'team',
        )


class UnitSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Unit
        exclude = (
            'team',
        )


class TenancySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Tenancy
