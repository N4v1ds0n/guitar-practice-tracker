from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.uploader import destroy
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.

class CustomUser(AbstractUser):
    def __str__(self):
        return self.username

