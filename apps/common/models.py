import uuid
from django.db import models
from django.utils.translation import ugettext_lazy as _
from softdelete.models import SoftDeleteObject

# Create your models here.
class TimeStampedModel(models.Model):
    """ TimeStampedModel
    An abstract base class model that provides self-managed "created" and
    "modified" fields.
    """
    created = models.DateTimeField(_('created'), auto_now_add=True)
    modified = models.DateTimeField(_('modified'), auto_now=True)

    class Meta:
        get_latest_by = 'modified'
        ordering = ('-modified', '-created',)
        abstract = True
        
        
class UUIDObject(TimeStampedModel, SoftDeleteObject):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4)
    
    class Meta:
        abstract=True