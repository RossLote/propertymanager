from django.db import models
from django_extensions.db.fields import AutoSlugField
from django.conf import settings
from common.models import TimeStampedSoftDeleteObject, SoftDeleteManager


class TeamManager(SoftDeleteManager):
    def create(self, user, name):
        team = super(TeamManager, self).create(name=name)
        team_user = team.users.create(
            user=user,
            admin=True
        )
        TeamOwner.objects.create(
            teamuser=team_user,
            team=team
        )
        return team


class Team(TimeStampedSoftDeleteObject):
    name = models.CharField(max_length=255)
    slug = AutoSlugField(populate_from='name')

    objects = TeamManager()

    def __unicode__(self):
        return self.slug

    @property
    def owner(self):
        return self.teamowner.teamuser.user


class TeamUser(TimeStampedSoftDeleteObject):
    team = models.ForeignKey(
        Team, related_name='users'
    )
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name='team_users'
    )
    admin = models.BooleanField()

    def __unicode__(self):
        return self.user.get_full_name()

    @property
    def is_owner(self):
        return hasattr(self, 'teamowner')

    @property
    def is_admin(self):
        return self.admin or self.is_owner


class TeamOwner(TimeStampedSoftDeleteObject):
    teamuser = models.OneToOneField(TeamUser)
    team = models.OneToOneField(Team)

    def __unicode__(self):
        return u'{} | {}'.format(
            self.teamuser, self.team
        )
