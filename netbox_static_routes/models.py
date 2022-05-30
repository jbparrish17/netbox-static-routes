#from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.postgres.fields import ArrayField
from netbox.models import NetBoxModel
from utilities.choices import ChoiceSet

# future use
class NextHopTypeChoices(ChoiceSet):
    key = 'StaticRoute.next_hop_type'

    NH_TYPE_IP_ADDRESS = ('ip_address', 'IP Address')
    NH_TYPE_INTERFACE = ('interface', 'Interface')
    NH_TYPE_VRF = ('vrf', 'VRF')

    CHOICES = [
        NH_TYPE_IP_ADDRESS,
        NH_TYPE_INTERFACE,
        NH_TYPE_VRF
    ]

class StaticRoute(NetBoxModel):
    site = models.ForeignKey(
        to='dcim.Site',
        on_delete=models.PROTECT,
        related_name="%(class)s_related",
        blank=True,
        null=True
    )
    device = models.ForeignKey(
        to='dcim.Device',
        on_delete=models.PROTECT,
        related_name='+',
        null=True,
    )
    vrf = models.ForeignKey(
        to='ipam.VRF',
        on_delete=models.PROTECT,
        related_name='+',
        blank=True,
        null=True,
        verbose_name='VRF'
    )
    destination_prefix = models.ForeignKey(
        to='ipam.Prefix',
        on_delete=models.PROTECT,
    )
    next_hop = ArrayField(
        base_field=models.GenericIPAddressField(),
    )
    distance = models.PositiveIntegerField(
        default=1,
        validators=[
            MinValueValidator(1),
            MaxValueValidator(255)
        ],
        verbose_name='Administrative distance'
    )
    comments = models.TextField(
        blank=True
    )

    class Meta:
        verbose_name_plural = 'Static Routes'
        ordering = ('device', 'vrf', 'destination_prefix', 'next_hop')
        unique_together = ['device', 'vrf', 'destination_prefix']

    def __str__(self):
        return f'{self.device}:{self.vrf}:{self.destination_prefix}'

    def get_absolute_url(self):
        return reverse('plugins:netbox_static_routes:staticroute', args=[self.pk])
