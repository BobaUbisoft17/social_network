from django.urls import path
from . import views


urlpatterns = [
    path("follower/<int:pk>", views.FollowerView.as_view()),
    path("<int:pk>", views.ListFollowersView.as_view()),
]
