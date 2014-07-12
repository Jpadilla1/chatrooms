from django.conf.urls import patterns, url

from rest_framework import routers

from .views import RoomViewSet
from ..messages.views import BroadcastRoomMessageView


router = routers.DefaultRouter()
router.register(r'rooms', RoomViewSet)

api_urlpatterns = router.urls

api_urlpatterns += patterns(
    '',
    url(
        r'^rooms/(?P<pk>[0-9]+)/send_message/$',
        BroadcastRoomMessageView.as_view(),
        name="send_message"
    ),
)
