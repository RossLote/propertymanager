from django.db import models
from common.models import UUIDObject
from softdelete.models import SoftDeleteObject, SoftDeleteManager
from .utils import COUNTRY_LIST, TITLE_LIST
from phonenumber_field.modelfields import PhoneNumberField

class Person(models.Model):
    title = models.PositiveSmallIntegerField(choices=TITLE_LIST)
    forename = models.CharField(max_length=40)
    middlenames = models.CharField(max_length=150, blank=True)
    surname = models.CharField(max_length=40)
    email = models.EmailField()
    phone = PhoneNumberField()

    class Meta:
        abstract = True


class Address(UUIDObject):
    team = models.ForeignKey('teams.Team', related_name='addresses')
    line_1 = models.CharField(max_length=100)
    line_2 = models.CharField(max_length=100, blank=True)
    line_3 = models.CharField(max_length=100, blank=True)
    town = models.CharField(max_length=50)
    county = models.CharField(max_length=50, blank=True)
    postcode = models.CharField(max_length=8)
    country = models.CharField(max_length=3, choices=COUNTRY_LIST)

    class Meta:
        verbose_name_plural = 'addresses'


class Landlord(UUIDObject):
    team = models.ForeignKey('teams.Team', related_name='landlords')
    address = models.ForeignKey('Address')


class Property(UUIDObject):
    hmo = models.BooleanField(default=False)
    team = models.ForeignKey('teams.Team', related_name='properties')
    address = models.ForeignKey('Address', related_name='properties')
    landlord = models.ForeignKey('Landlord', related_name='properties')
    gallery = models.ForeignKey('gallery.Gallery', related_name='properties')


class Room(UUIDObject):
    habitable = models.BooleanField(default=False)
    team = models.ForeignKey('teams.Team', related_name='rooms')
    property = models.ForeignKey('Property', related_name='rooms')
    gallery = models.ForeignKey('gallery.Gallery', related_name='rooms')


class Tenant(Person, UUIDObject):
    team = models.ForeignKey('teams.Team', related_name='tenants')
    dob = models.DateField(blank=True)


class Tenancy(UUIDObject):
    team = models.ForeignKey('teams.Team', related_name='tenancies')
    property = models.ForeignKey('Property', related_name='tenancies')
    room = models.ForeignKey(
        'Room', related_name='tenancies',
        default=None, null=True, blank=True
    )
    tenant = models.ForeignKey('Tenant', related_name='tenancies')
    start_date = models.DateField(blank=True)
    end_date = models.DateField(blank=True)

    class Meta:
        verbose_name_plural = 'Tenancies'
