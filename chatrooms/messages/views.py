from ..rooms.models import Room

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

from ws4redis.publisher import RedisPublisher


class BroadcastRoomMessageView(APIView):

    def post(self, request, pk, format=None):
        message = request.POST.get('message', '')

        if Room.objects.get(pk=pk) and message:
            data = {
                'room': pk,
                'message': message,
                'success': "true",
            }
            redis_publisher = RedisPublisher(
                facility='room-%d' % pk,
                users=[Room.objects.get(pk=pk).members],
                broadcast=True)
            redis_publisher.publish_message(message)
        else:
            data = {
                'error_message':
                "Error sending message=%s to room=%d" % (message, int(pk)),
                'success': "false"
            }

        return Response(data, status.HTTP_200_OK)
