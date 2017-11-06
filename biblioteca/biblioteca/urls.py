"""biblioteca URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from .views import home
from libros.views import lista_libros, detalle_libros
from libros.views import LibroCreateView, LibroDeleteView, LibroUpdateView, LibroListView


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^home/$', home, name='home'),
    url(r'^libros/lista$', LibroListView.as_view(), name='lista'),
    url(r'^libros/detalle/(?P<id>\d)/$', detalle_libros, name='detalles'),
    url(r'^libros/detalle/(?P<id>\d\d)/$', detalle_libros, name='detalles'),
    url(r'^libros/create$', LibroCreateView.as_view(), name='libros_create'),
    url(r'^libros/detalle/(?P<pk>\d)/edit', LibroUpdateView.as_view(), name='libros_mod'),
    url(r'^libros/detalle/(?P<pk>\d)/delete', LibroDeleteView.as_view(), name='libros_del'),
    url(r'^libros/detalle/(?P<pk>\d\d)/edit', LibroUpdateView.as_view(), name='libros_mod'),
    url(r'^libros/detalle/(?P<pk>\d\d)/delete', LibroDeleteView.as_view(), name='libros_del'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
