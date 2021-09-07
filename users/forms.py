from django import forms
from api.models import MobileMoneyUsersRegistration, AgencyBankingRegistration


class MobileMoneyForm(forms.ModelForm):

    class Meta:
        model = MobileMoneyUsersRegistration
        fields = ['network', 'phone', 'name', 'id_type', 'id_number', 'photo']


class AgencyBankingForm(forms.ModelForm):
    class Meta:
        model = AgencyBankingRegistration
        fields = ['bank', 'account_number', 'phone', 'name', 'id_type', 'id_number', 'photo']