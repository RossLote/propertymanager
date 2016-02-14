from rest_framework import serializers
from . import models


class LeaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Lease
