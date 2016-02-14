from __future__ import unicode_literals

from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.utils.translation import ugettext_lazy as _

from common.models import TimeStampedSoftDeleteObject

# Create your models here.
class Document(TimeStampedSoftDeleteObject):
    team = models.ForeignKey('teams.Team', related_name='documents')
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')
    title = models.CharField(
        _('title'), max_length=200,
        default=None, null=True, blank=True
    )
    file = models.FileField(
        _('File'),
        upload_to='documents'
    )
