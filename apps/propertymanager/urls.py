from django.conf.urls import include, url
from . import api_urls

urlpatterns = [
    url(r'^api/v1/', include(api_urls)),
]
