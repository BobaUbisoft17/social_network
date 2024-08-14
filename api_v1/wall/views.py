from rest_framework.generics import ListAPIView
from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
    AllowAny,
    BasePermission,
    SAFE_METHODS,
)
from rest_framework import permissions

from .classes import CreateRetrieveUpdateDestroy, CreateUpdateDestroy
from .models import Comment, Post
from .pagination import PostPagination, CommentPagination
from .serializers import CommentSerializer, ListPostSerealizer, PostSerializer


class ListPostView(ListAPIView):

    serializer_class = ListPostSerealizer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = PostPagination

    def get_queryset(self):
        return (
            Post.objects.filter(author_id=self.kwargs.get("pk"))
            .order_by("-create_date")
            .select_related("author")
            .prefetch_related("comments")
        )


class IsAuthor(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return obj.author == request.user


class PostView(CreateRetrieveUpdateDestroy):

    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Post.objects.all().select_related("author")
    permission_classes_by_action = {
        "get": [AllowAny],
        "put": [IsAuthor],
        "destroy": [IsAuthor],
    }

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentView(CreateUpdateDestroy):

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()
    permission_classes_by_action = {
        "update": [IsAuthor],
        "destroy": [IsAuthor],
    }

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_destroy(self, instance):
        instance.deleted = True
        instance.save()


class SubCommentView(ListAPIView):

    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    pagination_class = CommentPagination

    def get_queryset(self):
        return (
            Comment.objects.filter(parent_comment_id=self.kwargs.get("pk"))
            .order_by("-created_date")
        )
