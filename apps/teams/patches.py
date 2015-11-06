from django.contrib.auth import get_user_model
from . import models


def get_teams(self):
    return models.Team.objects.filter(users__user=self)


def get_teams_owned(self):
    return models.Team.objects.filter(teamowner__teamuser__user=self)


get_user_model().add_to_class('get_teams', get_teams)
get_user_model().add_to_class('get_teams_owned', get_teams_owned)