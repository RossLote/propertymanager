from __future__ import unicode_literals

from common.models import UUIDObject
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.dispatch import receiver
from django.db.models.signals import pre_save


class Gallery(UUIDObject):
    team = models.ForeignKey('teams.Team', related_name='galleries')
    title = models.CharField(
        _('title'), max_length=200,
    )

    def __unicode__(self):
        return self.title

    def get_main_image(self):
        return self.images.first()

    def get_images(self):

        return [image for image in self.images.all()]


class Image(UUIDObject):
    title = models.CharField(
        _('title'), max_length=200,
        default=None, null=True, blank=True
    )
    image = models.ImageField(
        _('Image'),
        upload_to='gallery/images'
    )
    gallery = models.ForeignKey(
        Gallery, verbose_name=_('Gallery'),
        related_name='images'
    )
    sort_order = models.PositiveSmallIntegerField(
        _('sort_order'), blank=True
    )

    class Meta:
        ordering = ['sort_order']
        unique_together=(
            ('gallery','sort_order'),
        )

    def get_image_url(self):
        return self.image.url

    def __unicode__(self):
        return self.image.url


@receiver(pre_save, sender=Image, dispatch_uid='0001')
def re_organise_sort_order(sender, instance, raw, using, **kwargs):
    images = instance.gallery.images

    if not instance.sort_order:
        highest = images.order_by('-sort_order').first()
        if highest:
            sort_order = highest.sort_order + 1
        else:
            sort_order = 1
        instance.sort_order = sort_order

    else:
        images = images.filter(sort_order__gte=instance.sort_order)
        if images.filter(sort_order=instance.sort_order):
            for image in images.order_by('-sort_order'):
                image.sort_order += 1
                image.save()
