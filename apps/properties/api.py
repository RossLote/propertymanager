from rest_framework import viewsets
from . import models, serializers


class TeamedObjectViewsetMixin(object):

    def get_queryset(self):

        return self.queryset.filter(
            team__users__user=self.request.user
        )

class PropertyViewset(TeamedObjectViewsetMixin, viewsets.ModelViewSet):

    queryset = models.Property.objects.all()
    serializer_class = serializers.PropertySerializer


class TenancyViewset(TeamedObjectViewsetMixin, viewsets.ModelViewSet):

    queryset = models.Tenancy.objects.all()
    serializer_class = serializers.TenancySerializer
