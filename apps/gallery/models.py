from __future__ import unicode_literals
from common.models import UUIDObject
from django.db import models

# Create your models here.
class Gallery(UUIDObject):
    # TODO: Define fields here

    class Meta:
        verbose_name = 'Gallery'
        verbose_name_plural = 'Galleries'

    def __unicode__(self):
        pass


class Image(UUIDObject):
    # TODO: Define fields here

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'

    def __unicode__(self):
        pass


class GalleryImage(UUIDObject):
    # TODO: Define fields here

    class Meta:
        verbose_name = 'GalleryImage'
        verbose_name_plural = 'GalleryImages'

    def __unicode__(self):
        pass
