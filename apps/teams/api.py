class TeamedObjectViewsetMixin(object):

    def get_queryset(self):

        return self.queryset.filter(
            team=self.request.team
        )
