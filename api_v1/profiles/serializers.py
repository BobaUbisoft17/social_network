from rest_framework import serializers
from .models import Profile


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        exclude = (
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "groups",
            "user_permissions",
        )


class PublicProfileSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(read_only=True)

    class Meta:
        model = Profile
        exclude = (
            "password",
            "last_login",
            "is_active",
            "is_staff",
            "is_superuser",
            "email",
            "groups",
            "user_permissions",
            "first_login",
        )


class UserByFollowerSerializer(serializers.ModelSerializer):
    avatar = serializers.ImageField(read_only=True, source="subscriber.avatar")
    username = serializers.ReadOnlyField(source="subscriber.username")

    class Meta:
        model = Profile
        fields = ('id', 'username', 'avatar')
