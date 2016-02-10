from rest_framework import viewsets
from . import models, serializers
from teams.api import TeamedObjectViewsetMixin


class OwnerViewset(TeamedObjectViewsetMixin, viewsets.ModelViewSet):

    queryset = models.Owner.objects.all()
    serializer_class = serializers.OwnerSerializer


class TenantViewset(TeamedObjectViewsetMixin, viewsets.ModelViewSet):

    queryset = models.Tenant.objects.all()
    serializer_class = serializers.TenantSerializer
