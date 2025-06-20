from django.contrib.auth.models import AbstractUser
from django.db import models
from cloudinary.uploader import destroy
from django.db.models.signals import post_delete
from django.dispatch import receiver

# Create your models here.

def user_photo_path(instance, filename):
    return f'user_images/{instance.username}/{filename}'


class CustomUser(AbstractUser):
    photo = models.ImageField(upload_to=user_photo_path, blank=True, null=True)

    def __str__(self):
        return self.username

@receiver(post_delete, sender=CustomUser)
def delete_user_photo(sender, instance, **kwargs):
    if instance.photo:
        public_id = instance.photo.name.rsplit('.', 1)[0]
        destroy(public_id)