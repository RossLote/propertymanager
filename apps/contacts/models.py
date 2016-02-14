from __future__ import unicode_literals

from django.db import models

from common.models import UUIDObject, TimeStampedSoftDeleteObject
from phonenumber_field.modelfields import PhoneNumberField
from softdelete.models import SoftDeleteObject, SoftDeleteManager
from .utils import TITLE_LIST
# Create your models here.


class Person(UUIDObject):
    title = models.PositiveSmallIntegerField(choices=TITLE_LIST)
    forename = models.CharField(max_length=40)
    middlenames = models.CharField(max_length=150, blank=True)
    surname = models.CharField(max_length=40)
    email = models.EmailField()
    phone = PhoneNumberField()

    class Meta:
        abstract = True


class Owner(Person):
    team = models.ForeignKey('teams.Team', related_name='landlords')

class Tenant(Person):
    team = models.ForeignKey('teams.Team', related_name='tenants')
