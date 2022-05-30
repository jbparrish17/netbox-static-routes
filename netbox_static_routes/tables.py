import django_tables2 as tables
from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import StaticRoute


class StaticRouteTable(NetBoxTable):
    pk = tables.Column(
        linkify=(
            'plugins:netbox_static_routes:staticroute-detail',
            kwargs={'pk': A.id}
        )
    )
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
        default_columns = ('pk', 'destination_prefix', 'site', 'device', 'vrf')
