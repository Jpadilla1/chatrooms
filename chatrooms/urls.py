from django.conf.urls import patterns, include, url
# from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api-v1/', include('chatrooms.router'))
)
