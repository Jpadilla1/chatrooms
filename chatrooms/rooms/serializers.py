from .models import Room

from rest_framework import serializers


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    created_by = serializers.SlugRelatedField(slug_field='username')

    class Meta:
        model = Room
        fields = ('id', 'url', 'title', 'created_by', 'created_at',
                  'members', 'is_private')
