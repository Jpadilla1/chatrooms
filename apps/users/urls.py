from django.conf.urls import patterns, url

from .views import MyRoomsView

urlpatterns = patterns(
    '',
    url(r'^rooms/', MyRoomsView.as_view(), name='myrooms'),
)
