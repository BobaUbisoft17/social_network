from rest_framework import permissions, response, viewsets

from api_v1.wall.models import Post
from api_v1.wall.serializers import ListPostSerealizer, PostSerializer


class FeedView(viewsets.ReadOnlyModelViewSet):

    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        instance = (
            Post.objects.filter(id=kwargs.get("pk"))
                .select_related("author")
                .prefetch_related("comments")
        )
        serializer = PostSerializer(instance)
        return response.Response(serializer.data)

    def list(self, request, *args, **kwargs):
        queryset = (
            Post.objects.filter(author__owner__subscriber=request.user)
            .order_by("-create_date")
            .select_related("author")
            .prefetch_related("comments")
        )
        serializer = ListPostSerealizer(queryset, many=True)
        return response.Response(serializer.data)
