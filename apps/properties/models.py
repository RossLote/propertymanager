from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from common.models import UUIDObject
from common.utils import Choices
from softdelete.models import SoftDeleteObject, SoftDeleteManager
from .utils import COUNTRY_LIST


class PropertyAttribute(SoftDeleteObject):
    name = models.CharField(max_length=100)


class Property(UUIDObject):
    team = models.ForeignKey('teams.Team', related_name='properties')
    name = models.CharField(max_length=150)
    street = models.CharField(max_length=100)
    town = models.CharField(max_length=50)
    county = models.CharField(max_length=50, blank=True)
    postcode = models.CharField(max_length=8)
    country = models.CharField(max_length=3, choices=COUNTRY_LIST)
    owner = models.ForeignKey('contacts.Owner', related_name='properties', null=True, blank=True, default=None)
    gallery = models.ForeignKey('gallery.Gallery', related_name='properties', null=True, blank=True, default=None)
    description = models.TextField(blank=True)
    attributes = models.ManyToManyField(PropertyAttribute)
    year_built = models.PositiveSmallIntegerField(blank=True, null=True, default=None)


class Document(SoftDeleteObject):
    team = models.ForeignKey('teams.Team', related_name='documents')
    property = models.ForeignKey('Property', related_name='documents')
    title = models.CharField(
        _('title'), max_length=200,
        default=None, null=True, blank=True
    )
    file = models.FileField(
        _('File'),
        upload_to='documents'
    )


class UnitAttribute(SoftDeleteObject):

    name = models.CharField(max_length=100)



class Unit(UUIDObject):
    PERIODS = Choices(
        (10, 'hour', _('hour')),
        (20, 'day', _('day')),
        (30, 'week', _('week')),
        (40, 'month', _('month')),
        (50, 'quarter', _('quarter')),
        (60, 'year', _('year')),
    )
    BEDS = Choices(
        (10, 'studio', _('studio')),
        (20, '1', _('1')),
        (30, '2', _('2')),
        (40, '3', _('3')),
        (50, '4', _('4')),
        (60, '5', _('5')),
        (70, '6', _('6')),
        (80, '7', _('7')),
        (90, '8', _('8')),
        (100, '9+', _('9+')),
    )
    BATHS = Choices(
        (10, 'shared', _('shared')),
        (20, '1', _('1')),
        (30, '2', _('2')),
        (40, '3', _('3')),
        (50, '4', _('4')),
        (60, '5+', _('5+')),
    )
    PARKING = Choices(
        (10, 'None', _('None')),
        (20, '1', _('1')),
        (30, '2', _('2')),
        (40, '3', _('3')),
        (50, '4', _('4')),
        (60, '5+', _('5+')),
    )
    TYPES = Choices(
        (10, 'apartment',   _('apartment')),
        (20, 'room',        _('room')),
        (30, 'duplex',      _('duplex')),
        (40, 'house',       _('house')),
        (50, 'townhouse',   _('townhouse')),
        (60, 'villa',       _('villa')),
        (70, 'office',      _('office')),
        (80, 'warehouse',   _('warehouse')),
        (90, 'storage',     _('storage')),
        (100, 'parking',    _('parking')),
    )
    team = models.ForeignKey('teams.Team', related_name='units')
    property = models.ForeignKey('Property', related_name='units')
    number = models.PositiveSmallIntegerField()
    type = models.PositiveSmallIntegerField(
        choices=TYPES, default=TYPES.apartment
    )
    size = models.DecimalField(max_digits=10, decimal_places=2)
    deposite = models.DecimalField(max_digits=8, decimal_places=2)
    rent = models.DecimalField(max_digits=8, decimal_places=2)
    period = models.PositiveSmallIntegerField(
        choices=PERIODS, default=PERIODS.month
    )
    beds = models.PositiveSmallIntegerField(
        choices=BEDS, default=BEDS['1']
    )
    bathrooms = models.PositiveSmallIntegerField(
        choices=BATHS, default=BATHS['1']
    )
    parking = models.PositiveSmallIntegerField(
        choices=PARKING, default=PARKING['1']
    )
    description = models.TextField(blank=True)
    attributes = models.ManyToManyField(UnitAttribute)
    pets = models.BooleanField(default=False)
    pet_policy = models.TextField(blank=True)


class Tenancy(UUIDObject):
    team = models.ForeignKey('teams.Team', related_name='tenancies')
    unit = models.ForeignKey('Unit', related_name='tenancies')
    tenant = models.ForeignKey('contacts.Tenant', related_name='tenancies')
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)

    class Meta:
        verbose_name_plural = 'Tenancies'
