import django_tables2 as tables
from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import StaticRoute

class StaticRouteTable(NetBoxTable):
    destination_prefix = tables.Column(
        linkify=True
    )
    site = tables.Column(
        linkify=True
    )
    device = tables.Column(
        linkify=True
    )
    vrf = tables.Column(
        linkify=True
    )

    class Meta(NetBoxTable.Meta):
        model = StaticRoute
        fields = ('pk', 'id', 'site', 'device', 'vrf', 'destination_prefix', 'next_hop', 'distance', 'comments')
        default_columns = ('destination_prefix', 'device', 'vrf')
