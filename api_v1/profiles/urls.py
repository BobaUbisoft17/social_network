from django.urls import path
from . import views


urlpatterns = [
    path("profile", views.ProfileView.as_view(
        {"get": "retrieve", "put": "update"})
    ),
    path("<int:pk>", views.PublicProfileView.as_view({"get": "retrieve"})),
]
