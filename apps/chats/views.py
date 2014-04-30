import datetime
import json

from dateutil.parser import parse
from django.views.generic import ListView, CreateView, DetailView
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.edit import FormMixin
from django.core import serializers

from braces.views import (LoginRequiredMixin, StaffuserRequiredMixin,
                          JSONResponseMixin, AjaxResponseMixin)

from ..messages.forms import CreateMessageForm
from ..messages.models import Message
from ..users.models import User
from .models import ChatRoom
from .forms import CreateRoomForm, EnrollRoomForm
from ..utils.utils import naturaltime


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


class RoomView(JSONResponseMixin, AjaxResponseMixin,
               LoginRequiredMixin, FormMixin, DetailView):
    model = ChatRoom
    form_class = CreateMessageForm
    template_name = "chats/room.html"

    def get_success_url(self):
        return redirect('chats:room', slug=self.kwargs['slug'])

    def get(self, request, *args, **kwargs):
        if ChatRoom.objects.filter(members=request.user, slug=kwargs['slug']):
            self.object = self.get_object()
            context = self.get_context_data(object=self.object)
            return self.render_to_response(context)
        else:
            return redirect('chats:check', slug=kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(RoomView, self).get_context_data(**kwargs)
        context['form'] = self.get_form(self.get_form_class())
        context['room'] = get_object_or_404(ChatRoom, slug=self.kwargs['slug'])
        context['room_messages'] = Message.objects.filter(room=context['room'])
        if context['room_messages'].count() > 0:
            context['room_message_last'] = context['room_messages'].last().id - 1
        users = User.objects.filter(
            last_login__gt=self.request.user.last_logged_out,
            is_active__exact=1, ).order_by('-last_login')
        context['online_users'] = users
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def get_ajax(self, request, *args, **kwargs):
        messages = Message.objects.filter(
            room__slug=kwargs['slug'])
        m = []
        for i in json.loads(serializers.serialize('json', messages)):
            i['fields']['created_by'] = get_object_or_404(
                User, pk=i['fields']['created_by']).username
            i['fields']['created_at'] = naturaltime(
                parse(i['fields']['created_at']))
            m.append(i['fields'])
        data = {
            'messages': json.dumps(m),
            'online_users': json.dumps(list(ChatRoom.objects.get(
                slug=kwargs['slug']).members.filter(
                    last_login__gt=self.request.user.last_logged_out,
                    is_active__exact=1, ).order_by(
                        '-last_login').values('username')))
        }
        if messages.count() > 0:
            data['last_message_id'] = messages.last().id - 1
        return self.render_json_response(data)

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        form.instance.created_at = datetime.datetime.now()
        form.instance.room = get_object_or_404(
            ChatRoom, slug=self.kwargs['slug'])
        form.save()
        return redirect('chats:room', slug=self.kwargs['slug'])


class EnrollRoomView(LoginRequiredMixin, FormMixin, DetailView):
    model = ChatRoom
    form_class = EnrollRoomForm
    template_name = "chats/enroll.html"

    def get_success_url(self):
        return redirect('chats:room', slug=self.kwargs['slug'])

    def get_context_data(self, **kwargs):
        context = super(EnrollRoomView, self).get_context_data(**kwargs)
        context['form'] = self.get_form(self.get_form_class())
        context['room'] = get_object_or_404(ChatRoom, slug=self.kwargs['slug'])
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        key = form.cleaned_data['key']
        room = get_object_or_404(ChatRoom, slug=self.kwargs['slug'])
        if room.key == key:
            room.members.add(self.request.user)
            room.save()
        else:
            print "The key given is not correct."
        return redirect('chats:room', slug=self.kwargs['slug'])
