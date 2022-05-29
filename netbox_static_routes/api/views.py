from netbox.api.viewsets import NetBoxModelViewSet
from .. import filtersets, models
from .serializers import StaticRouteSerializer

class StaticRouteViewSet(NetBoxModelViewSet):
    queryset = models.StaticRoute.objects.prefetch_related('tags')
    serializer_class = StaticRouteSerializer
    