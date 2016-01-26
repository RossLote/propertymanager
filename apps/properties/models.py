from django.db import models
from common.models import UUIDObject
from softdelete.models import SoftDeleteObject, SoftDeleteManager
from .utils import COUNTRY_LIST


class Property(UUIDObject):
    team = models.ForeignKey('teams.Team', related_name='properties')
    name = models.CharField(max_length=150)
    street = models.CharField(max_length=100)
    town = models.CharField(max_length=50)
    county = models.CharField(max_length=50, blank=True)
    postcode = models.CharField(max_length=8)
    country = models.CharField(max_length=3, choices=COUNTRY_LIST)
    ownder = models.ForeignKey('contacts.Owner', related_name='properties', null=True, blank=True, default=None)
    gallery = models.ForeignKey('gallery.Gallery', related_name='properties', null=True, blank=True, default=None)


class Tenancy(UUIDObject):
    team = models.ForeignKey('teams.Team', related_name='tenancies')
    property = models.ForeignKey('Property', related_name='tenancies')
    tenant = models.ForeignKey('contacts.Tenant', related_name='tenancies')
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)

    class Meta:
        verbose_name_plural = 'Tenancies'
