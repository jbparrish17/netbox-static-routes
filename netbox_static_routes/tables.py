import django_tables2 as tables
from netbox.tables import NetBoxTable, ChoiceFieldColumn
from .models import StaticRoute
from django.urls import path


class StaticRouteTable(NetBoxTable):
    destination_prefix = tables.Column(
        linkify=(
            ('plugins:netbox_static_routes:staticroute', {'pk': tables.A('pk')})
        )
    )
    next_hop = tables.Column()
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
        default_columns = ('pk', 'destination_prefix', 'next_hop', 'site', 'device', 'vrf')
