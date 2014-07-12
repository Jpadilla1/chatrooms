from django.conf.urls import patterns, include, url
# from django.views.generic import TemplateView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    url(r'^api-v1/', include('chatrooms.router')),
    url(r'^api-auth/',
        include('rest_framework.urls', namespace='rest_framework'))
)
