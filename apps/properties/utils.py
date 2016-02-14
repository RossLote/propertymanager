from django.utils.translation import ugettext_lazy as _
from common.utils import Choices

PAYMENT_PERIODS = Choices(
    (10, 'hour',        _('hourly')),
    (20, 'day',         _('daily')),
    (30, 'week',        _('weekly')),
    (40, 'fortnight',   _('every two weeks')),
    (50, 'month',       _('monthly')),
    (60, 'quarter',     _('quarterly')),
    (70, 'halfyear',    _('very six months')),
    (80, 'year',        _('yearly')),
    (90, 'oneoff',      _('one off')),
)

COUNTRY_LIST = (
    ('GBR' , _('United Kingdom')),
    ('USA' , _('United States of America')),
)
