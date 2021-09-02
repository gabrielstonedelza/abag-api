from django.db import models
from PIL import Image
from django.conf import settings
from django.utils import timezone

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

BANKS = (
    ("Absa", "Absa"),
    ("Access Bank", "Access Bank"),
    ("ADB", "ADB"),
    ("Bank of Africa", "Bank of Africa"),
    ("Cal Bank", "Cal Bank"),
    ("Consolidated Bank Ghana", "Consolidated Bank Ghana"),
    ("Fidelity Bank", "Fidelity Bank"),
    ("Ecobank", "Ecobank"),
    ("First Atlantic Bank", "First Atlantic Bank"),
    ("First Bank of Nigeria", "First Bank of Nigeria"),
    ("GCB Bank Ltd", "GCB Bank Ltd"),
    ("GHL Bank Ltd", "GHL Bank Ltd"),
    ("GT Bank", "GT Bank"),
    ("National Investment Bank", "National Investment Bank"),
    ("Prudential Bank", "Prudential Bank"),
    ("Republic Bank Limited", "Republic Bank Limited"),
    ("Sahel Sahara Bank", "Sahel Sahara Bank"),
    ("Societe General Ghana Ltd", "Societe General Ghana Ltd"),
    ("Stanbic Bank", "Stanbic Bank"),
    ("Standard Chartered Bank", "Standard Chartered Bank"),
    ("United Bank Of Africa", "United Bank Of Africa"),
    ("Universal Merchant Bank", "Universal Merchant Bank"),
    ("Zenith bank", "Zenith bank"),
)


class AgencyBankingRegistration(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    bank = models.CharField(max_length=100, choices=BANKS, default="GT Bank")
    phone = models.CharField(max_length=15)
    name = models.CharField(max_length=100, unique=True)
    id_type = models.CharField(max_length=100, choices=IDTYPE, default="Ghana National Card")
    id_number = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="agency_abanking", default="")
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_photo(self):
        if self.photo:
            return "https://www.africanbankersassociationofghana.xyz" + self.photo.url


class AgencyBankingDeposit(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    bank = models.CharField(max_length=100, choices=BANKS)
    account_number = models.CharField(max_length=200, default=0)
    phone = models.CharField(max_length=15)
    other_phone = models.CharField(max_length=15)
    name = models.CharField(max_length=100, unique=True)
    id_type = models.CharField(max_length=100, choices=IDTYPE)
    amount = models.FloatField()
    date_deposited = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class AgencyBankingWithDraw(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    bank = models.CharField(max_length=100, choices=BANKS)
    account_number = models.CharField(max_length=200, default=0)
    phone = models.CharField(max_length=15)
    amount = models.FloatField()
    date_withdrew = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone


class MobileMoneyUsersRegistration(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    network = models.CharField(max_length=11, choices=NETWORK, default="MTN")
    phone = models.CharField(max_length=15)
    name = models.CharField(max_length=100, unique=True)
    id_type = models.CharField(max_length=100, choices=IDTYPE, default="Ghana National Card")
    id_number = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="mobile_money", default="")
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_photo(self):
        if self.photo:
            return "https://www.africanbankersassociationofghana.xyz" + self.photo.url


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
    amount = models.FloatField()
    date_withdrew = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone


class Fraud(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    reason = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class MomoPay(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    network = models.CharField(max_length=100, choices=NETWORK)
    phone = models.CharField(max_length=15)
    amount = models.IntegerField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.phone
