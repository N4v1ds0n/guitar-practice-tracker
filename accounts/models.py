from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

def user_photo_path(instance, filename):
    return f'user_images/{instance.username}/{filename}'


class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to=user_photo_path, blank=True, null=True)

    def __str__(self):
        return self.username
