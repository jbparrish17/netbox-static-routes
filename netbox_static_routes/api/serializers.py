from rest_framework import serializers
from ipam.api.serializers import NestedPrefixSerializer
from netbox.api.serializers import NetBoxModelSerializer, WritableNestedSerializer
from ..models import StaticRoute

class NestedStaticRouteSerializer(WritableNestedSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_static_routes-api:staticroute-detail'
    )

    class Meta:
        model = StaticRoute
        fields = ('id', 'url', 'display', 'destination_prefix', 'next_hop', 'device', 'vrf')


class StaticRouteSerializer(NetBoxModelSerializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='plugins-api:netbox_access_lists-api:staticroute-detail'
    )

    class Meta:
        model = StaticRoute
        fields = (
            'id', 'display', 'destination_prefix', 'next_hop', 'site', 'device', 'vrf', 'comments', 'tags', 'custom_fields', 'created', 'last_updated'
        )