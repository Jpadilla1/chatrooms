from django.views.generic import ListView, CreateView, FormView
from django.shortcuts import redirect

from braces.views import LoginRequiredMixin, StaffuserRequiredMixin

from ..messages.forms import CreateMessageForm

from .models import ChatRoom
from .forms import CreateRoomForm


class RoomsView(LoginRequiredMixin, ListView):
    model = ChatRoom
    paginate_by = 10
    template_name = "chats/index.html"


class CreateRoomView(LoginRequiredMixin, StaffuserRequiredMixin, CreateView):
    model = ChatRoom
    form_class = CreateRoomForm
    template_name = "chats/create.html"

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        self.object = form.save()
        return redirect('users:myrooms')


class RoomView(LoginRequiredMixin, FormView):
    form_class = CreateMessageForm
    template_name = "chats/room.html"
