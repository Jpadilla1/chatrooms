from .models import Room

from rest_framework import viewsets

from .serializers import RoomSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    filter_fields = ('title', 'created_by__username', 'is_private')
    search_fields = ('title', 'created_by__username', 'is_private')
    ordering = ('title',)
    ordering_fields = ('title', 'created_by__username',
                       'is_private', 'created_at')
