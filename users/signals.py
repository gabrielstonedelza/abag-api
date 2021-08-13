from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.conf import settings

User = settings.AUTH_USER_MODEL


@receiver(post_save, sender=User)
def create_profile(sender, created, instance, **kwargs):
    if created:
        Profile.objects.create(user=instance)