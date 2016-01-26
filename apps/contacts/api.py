from rest_framework import viewsets
from . import models, serializers


class TeamedObjectViewsetMixin(object):

    def get_queryset(self):

        return self.queryset.filter(
            team__users__user=self.request.user
        )

\
class OwnerViewset(TeamedObjectViewsetMixin, viewsets.ModelViewSet):

    queryset = models.Owner.objects.all()
    serializer_class = serializers.OwnerSerializer


class TenantViewset(TeamedObjectViewsetMixin, viewsets.ModelViewSet):

    queryset = models.Tenant.objects.all()
    serializer_class = serializers.TenantSerializer
