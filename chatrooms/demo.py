from django.http import HttpResponse
from django.views.generic.base import TemplateView
from ws4redis.publisher import RedisPublisher


class DemoChatView(TemplateView):
    template_name = 'index.html'

    def post(self, request, *args, **kwargs):
        redis_publisher = RedisPublisher(
            facility='demo', broadcast=True)
        redis_publisher.publish_message(request.POST.get('message'))
        return HttpResponse('OK')
