from .models import TeamUser
from django.shortcuts import redirect

class TeamSubdomainMiddleware:
    """ Gets the subdomain and uses it to find the Team and TeamUser. Attaches them to the request object """

    def process_request(self, request):
        domain_parts = request.get_host().split('.')
        request.teamuser=None
        request.team=None
        if (len(domain_parts) > 2):
            subdomain = domain_parts[0]
            if (subdomain.lower() == 'www'):
                subdomain = None
            domain = '.'.join(domain_parts[1:])
        else:
            subdomain = None
            domain = request.get_host()
        if subdomain and request.user.is_authenticated():
            try:
                request.teamuser = TeamUser.objects.select_related('team').get(user=request.user, team__slug=subdomain)
                request.team = request.teamuser.team
            except TeamUser.DoesNotExist:
                return redirect('http://www.propertymanager.com:8000')
