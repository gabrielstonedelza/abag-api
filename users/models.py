from django.db import models
from PIL import Image
import random
from django.contrib.auth.models import AbstractUser
from django.conf import settings

DeUser = settings.AUTH_USER_MODEL

# Create your models here.
LOCAL_REGIONS = (
    ("Ashanti", "Ashanti"),
    ("Greater Accra", "Greater Accra"),
    ("Brong-Ahafo", "Brong-Ahafo"),
    ("Northern", "Northern"),
    ("Central", "Central"),
    ("Upper East", "Upper East"),
    ("Upper West", "Upper West"),
    ("Eastern", "Eastern"),
    ("Volta", "Volta"),
    ("Western", "Western")
)


class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)
    agent_code = models.CharField(max_length=11, unique=True)
    phone = models.CharField(max_length=15, unique=True)
    company_name = models.CharField(max_length=200)
    full_name = models.CharField(max_length=150, default="Abag User")
    region = models.CharField(max_length=50)
    regional_code = models.CharField(max_length=2)
    REQUIRED_FIELDS = ['username', 'email', 'phone', 'company_name', 'full_name']
    USERNAME_FIELD = 'agent_code'

    def get_agent_code(self):
        return self.agent_code

    def save(self, *args, **kwargs):
        r_code = ""
        if self.region == "Ashanti":
            r_code = "A"
        if self.region == "Greater Accra":
            r_code = "GR"
        if self.region == "Brong-Ahafo":
            r_code = "BA"
        if self.region == "Northern":
            r_code = "NR"
        if self.region == "Central":
            r_code = "CR"
        if self.region == "Upper East":
            r_code = "UE"
        if self.region == "Upper West":
            r_code = "UW"
        if self.region == "Eastern":
            r_code = "ER"
        if self.region == "Volta":
            r_code = "VR"
        if self.region == "Western":
            r_code = "WR"

        self.regional_code = r_code

        super().save(*args, **kwargs)


class Branch(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(unique=True, max_length=255)
    phone = models.CharField(max_length=15, unique=True)
    user_code = models.CharField(max_length=11, unique=True)
    full_name = models.CharField(max_length=150, default="Abag Agent User")

    def __str__(self):
        return self.agent.company_name


class AgentsReBalancing(models.Model):
    agent1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requesting_agent")
    agent2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accepting_agent")
    message = models.TextField()
    approved = models.BooleanField(default=False)
    date_requested = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message


class AuthenticatedPhoneAddress(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_mac_address = models.CharField(max_length=100)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone_mac_address
