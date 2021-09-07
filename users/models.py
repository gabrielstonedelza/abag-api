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
    agent_code = models.CharField(max_length=11, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    company_name = models.CharField(max_length=200)
    full_name = models.CharField(max_length=150, default="Abag User")
    REQUIRED_FIELDS = ['username', 'email', 'phone', 'company_name', 'full_name']
    USERNAME_FIELD = 'agent_code'

    def get_agent_code(self):
        return self.agent_code


class Branch(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, max_length=255)
    phone = models.CharField(max_length=15, unique=True)
    user_code = models.CharField(max_length=11, unique=True)
    full_name = models.CharField(max_length=150, default="Abag Agent User")

    def __str__(self):
        return self.agent.company_name


class AgentsRebalancing(models.Model):
    agent1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requesting_agent")
    agent2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accepting_agent")
    message = models.TextField()
    approved = models.BooleanField(default=False)
    date_requested = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
