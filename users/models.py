from django.db import models
from PIL import Image
import random
from django.contrib.auth.models import AbstractUser
from django.conf import settings

DeUser = settings.AUTH_USER_MODEL

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
           'W', 'X', 'Y', 'Z']


# Create your models here.

class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    agent_code = models.IntegerField(unique=True)
    phone = models.CharField(max_length=11, unique=True)
    REQUIRED_FIELDS = ['email', 'phone', 'username']
    USERNAME_FIELD = 'agent_code'

    def get_username(self):
        return self.agent_code


class Profile(models.Model):
    user = models.OneToOneField(DeUser, on_delete=models.CASCADE, related_name="profile_user")
    full_name = models.CharField(max_length=150, default="New User")
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True, default='user.png')
    company_name = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.user.username}"
