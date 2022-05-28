from dcim.models import Site, Device
from ipam.models import Prefix, VRF
from netbox.forms import NetBoxModelForm
from .models import StaticRoute
from utilities.forms.fields import CommentField, DynamicModelChoiceField

class StaticRouteForm(NetBoxModelForm):
    site = DynamicModelChoiceField(
        queryset=Site.objects.all(),
        required=False
    )
    device = DynamicModelChoiceField(
        queryset=Device.objects.all(),
        query_params={
            'site_id': '$site'
        }
    )
    vrf = DynamicModelChoiceField(
        queryset=VRF.objects.all(),
        required=False
    )
    # need to be able to handle no VRF
    destination_prefix = DynamicModelChoiceField(
        queryset=Prefix.objects.all(),
        query_params={
            'vrf_id': '$vrf'
        }
    )
    comments = CommentField()

    class Meta:
        model = StaticRoute
        fields = ('site', 'device', 'vrf', 'destination_prefix', 'next_hop', 'distance', 'comments', 'tags')

# filter form

# consider adding a bulk edit form