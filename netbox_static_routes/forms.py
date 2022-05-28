from dcim.models import Site, Device
from ipam.models import Prefix, VRF
from django import forms
from netbox.forms import NetBoxModelForm, NetBoxModelFilterSetForm
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

class StaticRouteFilterForm(NetBoxModelFilterSetForm):
    model = StaticRoute
    static_route = forms.ModelMultipleChoiceField(
        queryset=StaticRoute.objects.all(),
        required=False
    )
    site = forms.ModelMultipleChoiceField(
        queryset=Site.objects.all(),
        required=False
    )
    device = forms.ModelMultipleChoiceField(
        queryset=Device.objects.all(),
        required=False
    )
    vrf = forms.ModelMultipleChoiceField(
        queryset=VRF.objects.all(),
        required=False
    )
    destination_prefix = forms.ModelMultipleChoiceField(
        queryset=Prefix.objects.all(),
        required=False
    )

# consider adding a bulk edit form