from django.conf.urls import url
from django.views.generic.base import RedirectView
from .views import LibrosListAPIView, LibrosCreateAPIView

urlpatterns = [
    url(r'^$', LibrosListAPIView.as_view(), name='list_ajax'),
    url(r'^create/$', LibrosCreateAPIView.as_view(), name='create_ajax'),
]
