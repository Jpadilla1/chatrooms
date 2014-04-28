from django.views.generic import TemplateView

from braces.views import LoginRequiredMixin

from ..chats.models import ChatRoom


class MyRoomsView(LoginRequiredMixin, TemplateView):
    template_name = "users/myrooms.html"

    def get_context_data(self, **kwargs):
        if 'view' not in kwargs:
            kwargs['view'] = self
        kwargs['created_rooms'] = ChatRoom.objects.filter(
            created_by=self.request.user)
        kwargs['myrooms'] = ChatRoom.objects.filter(members=self.request.user)
        return kwargs
