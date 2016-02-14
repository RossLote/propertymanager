from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext_lazy as _
from common.models import TimeStampedSoftDeleteObject
from common.utils import Choices
from properties.utils import PAYMENT_PERIODS
from django.contrib.contenttypes.fields import GenericRelation

# Create your models here.
class Lease(TimeStampedSoftDeleteObject):
    PERIODS = PAYMENT_PERIODS
    TYPES = Choices(
        (10, 'fixed', _('fixed')),
        (20, 'month-to-month', _('month-to-month')),
    )

    team = models.ForeignKey('teams.Team', related_name='leases')
    unit = models.ForeignKey('properties.Unit', related_name='leases')
    tenant = models.ForeignKey('contacts.Tenant', related_name='leases')
    type = models.PositiveSmallIntegerField(choices=TYPES, default=TYPES.fixed)
    number = models.PositiveSmallIntegerField(default=1)
    start_date = models.DateField()
    end_date = models.DateField(blank=True)
    period = models.PositiveSmallIntegerField(choices=PERIODS, default=PERIODS.month)
    prorate = models.DecimalField(decimal_places=2, max_digits=8)
    late_payment_fee = models.BooleanField(default=False)
    documents = GenericRelation('documents.Document', related_query_name='leases')

    # UTILITIES (None = N/A, True = Landlord, False = Tenant)
    gas =           models.NullBooleanField(default=None)
    electric =      models.NullBooleanField(default=None)
    water =         models.NullBooleanField(default=None)
    tv =            models.NullBooleanField(default=None)
    garbage =       models.NullBooleanField(default=None)
    hoa =           models.NullBooleanField(default=None) # home owners association / factor
    internet =      models.NullBooleanField(default=None)
    council_tax =   models.NullBooleanField(default=None)
    landscaping =   models.NullBooleanField(default=None)
    gas =           models.NullBooleanField(default=None)

    class Meta:
        verbose_name_plural = 'leases'


class LeaseFees(TimeStampedSoftDeleteObject):
    TYPES = Choices(
        (10, 'rent', _('rent')),
    )
    SCHEDULE = PAYMENT_PERIODS
    team = models.ForeignKey('teams.Team', related_name='leasefees')
    lease = models.ForeignKey('Lease', related_name='leasefees')
    type = models.PositiveSmallIntegerField(choices=TYPES, default=TYPES.rent)
    schedule = models.PositiveSmallIntegerField(choices=SCHEDULE)
    amount = models.DecimalField(decimal_places=2, max_digits=8)
    due_date = models.DateField()
