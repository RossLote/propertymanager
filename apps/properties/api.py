from rest_framework import viewsets
from . import models, serializers
from teams.api import TeamedObjectViewsetMixin
from rest_framework import filters


class PropertyViewset(TeamedObjectViewsetMixin, viewsets.ModelViewSet):

    queryset = models.Property.objects.all()
    serializer_class = serializers.PropertySerializer

    def perform_create(self, serializer):
        serializer.save(team=self.request.team)


class UnitFilter(filters.FilterSet):

    class Meta:
        model = models.Unit
        fields = ('property',)


class UnitViewset(TeamedObjectViewsetMixin, viewsets.ModelViewSet):

    queryset = models.Unit.objects.all()
    serializer_class = serializers.UnitSerializer
    filter_class = UnitFilter

    def perform_create(self, serializer):
        serializer.save(team=self.request.team)


class TenancyViewset(TeamedObjectViewsetMixin, viewsets.ModelViewSet):

    queryset = models.Tenancy.objects.all()
    serializer_class = serializers.TenancySerializer
