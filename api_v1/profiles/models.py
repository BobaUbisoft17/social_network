from django.db import models
from django.contrib.auth.models import AbstractUser


class Profile(AbstractUser):

    Gender = (
        ("male", "male"),
        ("female", "female")
    )
    birthday = models.DateField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    first_login = models.DateTimeField(blank=True, null=True)
    gender = models.CharField(max_length=6, choices=Gender, default="male")
    avatar = models.ImageField(upload_to="user/avatar/", blank=True, null=True)
