from rest_framework import serializers

from .models import Follower
from api_v1.profiles.serializers import UserByFollowerSerializer


class ListFollowerSerializer(serializers.ModelSerializer):
    subscribers = UserByFollowerSerializer(
        many=True,
        read_only=True,
        source="subscriber.subscribers",
    )

    class Meta:
        model = Follower
        fields = ("subscribers",)
