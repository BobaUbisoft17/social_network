from rest_framework import serializers

from .models import Comment, Post


class FilterCommentListSerializer(serializers.ListSerializer):

    def to_representation(self, data):
        data = data.filter(parent_comment_id=None)
        return super().to_representation(data)


class CommentSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Comment
        fields = ("author", "parent_post", "text", "parent_comment")


class ListCommentSerializer(serializers.ModelSerializer):

    text = serializers.SerializerMethodField()
    author = serializers.ReadOnlyField(source="author.username")

    def get_text(self, obj):
        if obj.deleted:
            return None
        return obj.text

    class Meta:
        list_serializer_class = FilterCommentListSerializer
        model = Comment
        fields = (
            "id",
            "text",
            "created_date",
            "author",
            "updated_date",
            "published",
            "deleted",
        )


class ListPostSerealizer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source="author.username")

    class Meta:
        model = Post
        fields = (
            "id",
            "create_date",
            "author",
            "text",
            "photo",
            "comments_count",
            "views_amount",
        )


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source="author.username")
    comments = ListCommentSerializer(many=True, read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "text",
            "photo",
            "create_date",
            "author",
            "comments",
            "views_amount",
        )
