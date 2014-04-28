from django.conf.urls import patterns, url

from .views import RoomsView, CreateRoomView, RoomView, EnrollRoomView

urlpatterns = patterns(
    '',
    url(r'^$', RoomsView.as_view(), name='index'),
    url(r'^create/$', CreateRoomView.as_view(), name='create'),
    url(r'^(?P<slug>[-\w]+)/$', RoomView.as_view(), name='room'),
    url(r'^(?P<slug>[-\w]+)/check/$', EnrollRoomView.as_view(), name='check'),
)
