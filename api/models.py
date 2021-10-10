from django.db import models
from django.conf import settings
from django.utils import timezone

User = settings.AUTH_USER_MODEL

NETWORK = (
    ("MTN", "MTN"),
    ("VODAFONE", 'VODAFONE'),
    ("AIRTELTIGO", 'AIRTELTIGO')
)

IDTYPE = (
    ("None", "None"),
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

    def get_photo(self):
        if self.photo:
            return "https://www.africanbankersassociationofghana.xyz" + self.photo.url


class AgencyBankingDeposit(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    bank = models.CharField(max_length=100, choices=BANKS)
    beneficiary_account_number = models.CharField(max_length=15)
    beneficiary_name = models.CharField(max_length=100)
    depositor_number = models.CharField(max_length=15)
    depositor_id_type = models.CharField(max_length=100, choices=IDTYPE, blank=True, default="")
    depositor_id_number = models.CharField(max_length=16, blank=True)
    amount = models.CharField(max_length=500)
    date_deposited = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.beneficiary_name


class AgencyBankingWithDraw(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    bank = models.CharField(max_length=100, choices=BANKS)
    account_number = models.CharField(max_length=15)
    amount = models.CharField(max_length=500)
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

    def get_photo(self):
        if self.photo:
            return "https://www.africanbankersassociationofghana.xyz" + self.photo.url


class MobileMoneyDeposit(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    network = models.CharField(max_length=11, choices=NETWORK)
    beneficiary_phone = models.CharField(max_length=15)
    beneficiary_name = models.CharField(max_length=100)
    depositor_phone = models.CharField(max_length=15)
    depositor_id_type = models.CharField(max_length=100, choices=IDTYPE, blank=True, default="None")
    depositor_number = models.CharField(max_length=16, blank=True)
    amount = models.CharField(max_length=500)
    date_deposited = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.beneficiary_name


class MobileMoneyWithDraw(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    network = models.CharField(max_length=11, choices=NETWORK)
    phone = models.CharField(max_length=15)
    amount = models.CharField(max_length=500)
    date_withdrew = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.phone


class Fraud(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    phone = models.CharField(max_length=15, unique=True)
    reason = models.TextField()
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class MomoPay(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    network = models.CharField(max_length=100, choices=NETWORK)
    phone = models.CharField(max_length=15)
    amount = models.CharField(max_length=500)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.phone


class AgentsAccountsStartedWith(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    mtn_physical = models.IntegerField()
    mtn_eCash = models.IntegerField()
    vodafone_physical = models.IntegerField()
    vodafone_eCash = models.IntegerField()
    airtel_tigo_physical = models.IntegerField()
    airtel_tigo_eCash = models.IntegerField()
    ecobank_physical = models.IntegerField()
    ecobank_eCash = models.IntegerField()
    calbank_physical = models.IntegerField()
    calbank_eCash = models.IntegerField()
    fidelity_physical = models.IntegerField()
    fidelity_eCash = models.IntegerField()
    date_started = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.agent.agent_code} has started accounts today"

    def physical_sum(self):
        return self.mtn_physical + self.vodafone_physical + self.airtel_tigo_physical + self.ecobank_physical + self.calbank_physical + self.fidelity_physical

    def ecash_sum(self):
        return self.mtn_eCash + self.vodafone_eCash + self.airtel_tigo_eCash + self.ecobank_eCash + self.calbank_eCash + self.fidelity_eCash


class AgentsAccountsCompletedWith(models.Model):
    agent = models.ForeignKey(User, on_delete=models.CASCADE)
    mtn_physical = models.IntegerField()
    mtn_eCash = models.IntegerField()
    vodafone_physical = models.IntegerField()
    vodafone_eCash = models.IntegerField()
    airtel_tigo_physical = models.IntegerField()
    airtel_tigo_eCash = models.IntegerField()
    ecobank_physical = models.IntegerField()
    ecobank_eCash = models.IntegerField()
    calbank_physical = models.IntegerField()
    calbank_eCash = models.IntegerField()
    fidelity_physical = models.IntegerField()
    fidelity_eCash = models.IntegerField()
    date_closed = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.agent.agent_code} has ended accounts today"

    def physical_sum(self):
        return self.mtn_physical + self.vodafone_physical + self.airtel_tigo_physical + self.ecobank_physical + self.calbank_physical + self.fidelity_physical

    def ecash_sum(self):
        return self.mtn_eCash + self.vodafone_eCash + self.airtel_tigo_eCash + self.ecobank_eCash + self.calbank_eCash + self.fidelity_eCash