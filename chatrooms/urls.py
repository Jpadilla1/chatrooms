from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from .demo import DemoChatView

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', DemoChatView.as_view(), name='index'),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^api-v1/', include('chatrooms.router')),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'))
)
