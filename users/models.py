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
    regional_code = models.CharField(max_length=2, blank=True)
    agent_display_code = models.CharField(max_length=200, blank=True)
    REQUIRED_FIELDS = ['username', 'email', 'phone', 'company_name', 'full_name']
    USERNAME_FIELD = 'agent_code'

    def get_agent_code(self):
        return self.agent_code

    def save(self, *args, **kwargs):
        acode = 0
        grcode = 0
        bacode = 0
        nrcode = 0
        crcode = 0
        uecode = 0
        uwcode = 0
        ercode = 0
        vrcode = 0
        wrcode = 0
        r_code = ""
        if self.region == "Ashanti":
            acode += 1
            r_code = "0000A"
            self.agent_display_code = r_code + str(acode)
        if self.region == "Greater Accra":
            grcode += 1
            r_code = "0000GR"
            self.agent_display_code = r_code + str(grcode)
        if self.region == "Brong-Ahafo":
            bacode += 1
            r_code = "0000BA"
            self.agent_code = r_code + str(bacode)
        if self.region == "Northern":
            nrcode += 1
            r_code = "0000NR"
            self.agent_code = r_code + str(nrcode)
        if self.region == "Central":
            crcode += 1
            r_code = "0000CR"
            self.agent_code = r_code + str(crcode)
        if self.region == "Upper East":
            uecode += 1
            r_code = "0000UE"
            self.agent_code = r_code + str(uecode)
        if self.region == "Upper West":
            uwcode += 1
            r_code = "0000UW"
            self.agent_code = r_code + str(uwcode)
        if self.region == "Eastern":
            ercode += 1
            r_code = "0000ER"
            self.agent_code = r_code + str(ercode)
        if self.region == "Volta":
            vrcode += 1
            r_code = "0000VR"
            self.agent_code = r_code + str(vrcode)
        if self.region == "Western":
            wrcode += 1
            r_code = "0000WR"
            self.agent_code = r_code + str(wrcode)

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
