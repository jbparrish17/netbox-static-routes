#from django.contrib.postgres.fields import ArrayField
from django.db import models
from django.urls import reverse
from netbox.models import NetBoxModel

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
        null=True
    )
    next_hop = models.GenericIPAddressField() # will want to add validators here to ensure v4 next-hop for v4 prefix and v6 next-hop for v6 prefix
    distance = models.PositiveIntegerField() # will want to add validators to limit integer
    comments = models.TextField(
        blank=True
    )

    class Meta:
        verbose_name_plural = 'Static Routes'
        unique_together = ['device', 'vrf', 'destination_prefix']

    def __str__(self):
        return f'{self.device}:{self.name}'

    def get_absolute_url(self):
        return reverse('plugins:netbox_static_routes:staticroute', args=[self.pk])
