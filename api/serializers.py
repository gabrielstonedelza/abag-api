from rest_framework import serializers
from .models import (MobileMoneyUsersRegistration, MobileMoneyDeposit, MobileMoneyWithDraw, AgencyBankingRegistration,
                     AgencyBankingDeposit, AgencyBankingWithDraw, Fraud, MomoPay, AgentsAccountsStartedWith,
                     AgentsAccountsCompletedWith)


class AgencyBankingSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = AgencyBankingRegistration
        fields = ['id', 'agent', 'username', 'bank', 'phone', 'name', 'id_type', 'id_number',
                  'date_registered', 'get_photo', 'photo', 'account_number']
        read_only_fields = ['agent']

    def get_username(self, agencyUser):
        username = agencyUser.agent.username
        return username


class AgencyBankingDepositSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = AgencyBankingDeposit
        fields = ['id', 'agent', 'username', 'bank', 'beneficiary_account_number', 'beneficiary_name',
                  'depositor_number', 'depositor_id_type', 'depositor_id_number', 'amount',
                  'date_deposited']
        read_only_fields = ['agent']

    def get_username(self, aDeposit):
        username = aDeposit.agent.username
        return username


class AgencyBankingWithDrawSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = AgencyBankingWithDraw
        fields = ['id', 'agent', 'username', 'bank', 'account_number', 'amount', 'date_withdrew']
        read_only_fields = ['agent']

    def get_username(self, mm_user):
        username = mm_user.agent.username
        return username


class MobileMoneyRegistrationSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = MobileMoneyUsersRegistration
        fields = ['id', 'agent', 'username', 'network', 'phone', 'name', 'id_type', 'id_number',
                  'date_registered', 'get_photo', 'photo']
        read_only_fields = ['agent']

    def get_username(self, mm_user):
        username = mm_user.agent.username
        return username


class MobileMoneyDepositSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = MobileMoneyDeposit
        fields = ['id', 'agent', 'username', 'network', 'beneficiary_phone', 'beneficiary_name', 'depositor_phone',
                  'depositor_id_type', 'depositor_number', 'amount',
                  'date_deposited', ]
        read_only_fields = ['agent']

    def get_username(self, mm_user):
        username = mm_user.agent.username
        return username


class MobileMoneyWithDrawSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = MobileMoneyWithDraw
        fields = ['id', 'agent', 'username', 'network', 'phone', 'amount', 'date_withdrew', ]
        read_only_fields = ['agent']

    def get_username(self, mm_user):
        username = mm_user.agent.username
        return username


class FraudSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')
    agent_display_code = serializers.SerializerMethodField('get_agent_display_code')
    agent_phone = serializers.SerializerMethodField('get_agent_phone')

    class Meta:
        model = Fraud
        fields = ['id', 'agent', 'username', 'agent_phone', 'agent_display_code', 'name', 'phone', 'reason',
                  'date_added']
        read_only_fields = ['agent']

    def get_username(self, mm_user):
        username = mm_user.agent.username
        return username

    def get_agent_display_code(self, mm_user):
        agent_display_code = mm_user.agent.agent_display_code
        return agent_display_code

    def get_agent_phone(self, mm_user):
        agent_phone = mm_user.agent.phone
        return agent_phone


class MomoPaySerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = MomoPay
        fields = ['id', 'agent', 'username', 'network', 'phone', 'amount', 'date_added']
        read_only_fields = ['agent']

    def get_username(self, mm_user):
        username = mm_user.agent.username
        return username


class AgentAccountsStartedSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = AgentsAccountsStartedWith
        fields = ['id', 'agent', 'username', 'physical_cash', 'mtn_eCash', 'vodafone_eCash',
                  'airtel_tigo_eCash', 'ecobank_eCash',
                  'calbank_eCash', 'fidelity_eCash', 'ecash_sum', 'date_started']
        read_only_fields = ['agent']

    def get_username(self, mm_user):
        username = mm_user.agent.username
        return username


class AgentAccountsCompletedSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = AgentsAccountsCompletedWith
        fields = ['id', 'agent', 'username', 'physical_cash', 'mtn_eCash', 'vodafone_eCash',
                  'airtel_tigo_eCash', 'ecobank_eCash',
                  'calbank_eCash', 'fidelity_eCash', 'ecash_sum', 'date_closed']
        read_only_fields = ['agent']

    def get_username(self, mm_user):
        username = mm_user.agent.username
        return username
