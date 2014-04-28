from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('allauth.urls')),
    url(r'^accounts/', include('apps.users.urls', namespace="users")),
    url(r'^chats/', include('apps.chats.urls', namespace="chats")),
)
