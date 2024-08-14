from django.urls import path
from . import views


urlpatterns = [
    path("<int:pk>", views.ListPostView.as_view()),
    path("post", views.PostView.as_view({"post": "create"})),
    path(
        "post/<int:pk>",
        views.PostView.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
    path("comment", views.CommentView.as_view({"post": "create"})),
    path(
        "comment/<int:pk>",
        views.CommentView.as_view(
            {"get": "retrieve", "put": "update", "delete": "destroy"}
        ),
    ),
    path("subcomment/<int:pk>", views.SubCommentView.as_view()),
]
