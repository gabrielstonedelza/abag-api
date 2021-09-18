from django.db import models
from PIL import Image
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

NETWORK = (
    ("MTN", "MTN"),
    ("VODAFONE", 'VODAFONE'),
    ("AIRTELTIGO", 'AIRTELTIGO')
)

IDTYPE = (
    ("Passport", "Passport"),
    ("Voters Id", "Voters Id"),
    ("Health Insurance", "Health Insurance"),
    ("Driving License", "Driving License"),
    ("Ghana National Card", "Ghana National Card"),
    ("SSNIT Card", "SSNIT Card"),
)

BANKS = (
    ("Access Bank", "Access Bank"),
    ("Cal Bank", "Cal Bank"),
    ("Fidelity Bank", "Fidelity Bank"),
    ("Ecobank", "Ecobank"),
    ("First Bank of Nigeria", "First Bank of Nigeria"),
    ("SGSSB", "SGSSB")
)


class AgencyBankingRegistration(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    bank = models.CharField(max_length=100, choices=BANKS, default="GT Bank")
    account_number = models.CharField(max_length=13, default=0)
    phone = models.CharField(max_length=15)
    name = models.CharField(max_length=100, unique=True)
    id_type = models.CharField(max_length=100, choices=IDTYPE, default="Ghana National Card")
    id_number = models.CharField(max_length=16)
    photo = models.ImageField(upload_to="agency_abanking", default="")
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.phone = self.phone[1:]
        super().save(*args, **kwargs)

    def get_photo(self):
        if self.photo:
            return "https://www.africanbankersassociationofghana.xyz" + self.photo.url


class AgencyBankingDeposit(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    bank = models.CharField(max_length=100, choices=BANKS)
    beneficiary_account_number = models.CharField(max_length=15)
    beneficiary_name = models.CharField(max_length=100)
    depositor_number = models.CharField(max_length=15)
    depositor_id_type = models.CharField(max_length=100, choices=IDTYPE)
    depositor_id_number = models.CharField(max_length=16)
    amount = models.FloatField()
    date_deposited = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.beneficiary_name


class AgencyBankingWithDraw(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    bank = models.CharField(max_length=100, choices=BANKS)
    account_number = models.CharField(max_length=15)
    amount = models.FloatField()
    date_withdrew = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.account_number


class MobileMoneyUsersRegistration(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    network = models.CharField(max_length=11, choices=NETWORK, default="MTN")
    phone = models.CharField(max_length=15)
    name = models.CharField(max_length=100, unique=True)
    id_type = models.CharField(max_length=100, choices=IDTYPE, default="Ghana National Card")
    id_number = models.CharField(max_length=16)
    photo = models.ImageField(upload_to="mobile_money", default="")
    date_registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.phone = self.phone[1:]
        super().save(*args, **kwargs)

    def get_photo(self):
        if self.photo:
            return "https://www.africanbankersassociationofghana.xyz" + self.photo.url


class MobileMoneyDeposit(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    network = models.CharField(max_length=11, choices=NETWORK)
    beneficiary_phone = models.CharField(max_length=15)
    beneficiary_name = models.CharField(max_length=100)
    depositor_phone = models.CharField(max_length=15)
    depositor_id_type = models.CharField(max_length=100, choices=IDTYPE, blank=True)
    depositor_number = models.CharField(max_length=16, blank=True)
    amount = models.FloatField()
    date_deposited = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.beneficiary_name


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


class ChatMessage(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sender", null=True)
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="receiver", null=True)
    message_id = models.CharField(max_length=20)
    message = models.TextField()
    date_messaged = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message
