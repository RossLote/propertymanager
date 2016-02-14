from rest_framework import viewsets
from . import models, serializers
from teams.api import TeamedObjectViewsetMixin
from rest_framework import filters


class LeaseViewset(TeamedObjectViewsetMixin, viewsets.ModelViewSet):

    queryset = models.Lease.objects.all()
    serializer_class = serializers.LeaseSerializer
