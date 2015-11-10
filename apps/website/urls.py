from django.conf.urls import url
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    url(r'^$',
        TemplateView.as_view(template_name='website/home.html'),
        name='password_reset_complete'),
]