from django.conf import settings
from django.db import models


class Post(models.Model):
    text = models.TextField(max_length=2048)
    photo = models.ImageField(upload_to="user/photo/", null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)
    views_amount = models.IntegerField(default=0)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    def comments_count(self) -> None:
        return self.comments.count()


class Comment(models.Model):
    text = models.TextField(max_length=1024)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)
    parent_post = models.ForeignKey(
        Post,
        related_name="comments",
        on_delete=models.CASCADE,
    )

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )

    parent_comment = models.ForeignKey(
        "self",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )
