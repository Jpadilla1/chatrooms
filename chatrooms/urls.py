from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$',
        TemplateView.as_view(template_name='static/index.html'),
        name='home'),

    url(r'^about/$',
        TemplateView.as_view(template_name='static/about.html'),
        name='about'),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/', include('apps.users.urls', namespace="users")),
    url(r'^chats/', include('apps.chats.urls', namespace="chats")),
)
