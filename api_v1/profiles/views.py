from django.shortcuts import get_object_or_404
from rest_framework import permissions
from rest_framework.viewsets import ModelViewSet

from .models import Profile
from .serializers import ProfileSerializer, PublicProfileSerializer


class PublicProfileView(ModelViewSet):
    serializer_class = PublicProfileSerializer
    permission_classes = [permissions.AllowAny]
    queryset = Profile.objects.all()


class ProfileView(ModelViewSet):
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Profile.objects.filter(id=self.request.user.id)

    def get_object(self):
        return get_object_or_404(
            self.get_queryset(),
            username=self.request.user,
        )
