"""stroykapremont URL Configuration

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
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic import RedirectView, TemplateView

from stroykapremont import settings

from landing_page import urls as base_urls, views

# from . import views
# from stroykapremont.views import home_view

# favicon_view = RedirectView.as_view(url='/static/favicons/favicon.ico', permanent=True)

urlpatterns = [
    # url(r'^favicon\.ico$', 'django.views.generic.simple.redirect_to', {'url': '/static/images/favicon.ico'}),
    # url(r'^favicon\.ico$', favicon_view),

    url(r'^$', views.home, name='home'),

    url(r'^ru/$', views.page),
    url(r'^en/$', views.page),


    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
