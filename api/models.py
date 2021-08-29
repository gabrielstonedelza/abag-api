from django.db import models
from PIL import Image
from django.conf import settings

User = settings.AUTH_USER_MODEL

NETWORK = (
    ("MTN", "MTN"),
    ("VODAFONE", 'VODAFONE'),
    ("AIRTEL TIGO", 'AIRTEL TIGO')
)

IDTYPE = (
    ("Passport", "Passport"),
    ("Voter's Id", "Voter's Id"),
    ("Health Insurance", "Health Insurance"),
    ("Driving License", "Driving License"),
    ("Ghana National Card", "Ghana National Card"),
    ("SSNIT Card", "SSNIT Card"),
)


class MobileMoneyUsersRegistration(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    network = models.CharField(max_length=11, choices=NETWORK, default="MTN")
    phone = models.CharField(max_length=15)
    name = models.CharField(max_length=100, unique=True)
    id_type = models.CharField(max_length=100, choices=IDTYPE, default="Ghana National Card")
    id_number = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="mobile_money_users", default="")
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class MobileMoneyDeposit(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    network = models.CharField(max_length=11, choices=NETWORK)
    phone = models.CharField(max_length=15)
    other_phone = models.CharField(max_length=15)
    name = models.CharField(max_length=100, unique=True)
    id_type = models.CharField(max_length=100, choices=IDTYPE)
    amount = models.FloatField()
    date_deposited = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class MobileMoneyWithDraw(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    network = models.CharField(max_length=11, choices=NETWORK)
    phone = models.CharField(max_length=15)
    name = models.CharField(max_length=100, unique=True)
    id_type = models.CharField(max_length=100, choices=IDTYPE)
    amount = models.FloatField()
    date_withdrew = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
