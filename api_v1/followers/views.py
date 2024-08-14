from rest_framework.generics import ListAPIView
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Follower
from .serializers import ListFollowerSerializer
from api_v1.profiles.models import Profile


class FollowerView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        try:
            user = Profile.objects.get(id=pk)
        except Profile.DoesNotExist:
            return Response(status=404)
        Follower.objects.create(subscriber=request.user, user=user)
        return Response(status=201)

    def delete(self, request, pk):
        try:
            sub = Follower.objects.get(user_id=pk, subscriber=request.user)
        except Follower.DoesNotExist:
            return Response(status=404)
        sub.delete()
        return Response(status=204)


class ListFollowersView(ListAPIView):
    serializer_class = ListFollowerSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_queryset(self):
        return Follower.objects.filter(user_id=self.kwargs.get("pk"))
