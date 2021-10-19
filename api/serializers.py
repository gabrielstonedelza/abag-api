from rest_framework import serializers
from .models import (MobileMoneyUsersRegistration, MobileMoneyDeposit, MobileMoneyWithDraw, AgencyBankingRegistration,
                     AgencyBankingDeposit, AgencyBankingWithDraw, Fraud, MomoPay, AgentsAccountsStartedWith,
                     AgentsAccountsCompletedWith)


class AgencyBankingSerializer(serializers.ModelSerializer):
    agent_code = serializers.SerializerMethodField('get_agent_code')

    class Meta:
        model = AgencyBankingRegistration
        fields = ['id', 'agent', 'agent_code', 'bank', 'phone', 'name', 'id_type', 'id_number',
                  'date_registered', 'get_photo', 'photo', 'account_number']
        read_only_fields = ['agent']

    def get_agent_code(self, agencyUser):
        agent_code = agencyUser.agent.agent_code
        return agent_code


class AgencyBankingDepositSerializer(serializers.ModelSerializer):
    agent_code = serializers.SerializerMethodField('get_agent_code')

    class Meta:
        model = AgencyBankingDeposit
        fields = ['id', 'agent', 'agent_code', 'bank', 'beneficiary_account_number', 'beneficiary_name',
                  'depositor_number', 'depositor_id_type', 'depositor_id_number', 'amount',
                  'date_deposited']
        read_only_fields = ['agent']

    def get_agent_code(self, aDeposit):
        agent_code = aDeposit.agent.agent_code
        return agent_code


class AgencyBankingWithDrawSerializer(serializers.ModelSerializer):
    agent_code = serializers.SerializerMethodField('get_agent_code')

    class Meta:
        model = AgencyBankingWithDraw
        fields = ['id', 'agent', 'agent_code', 'bank', 'account_number', 'amount', 'date_withdrew']
        read_only_fields = ['agent']

    def get_agent_code(self, mm_user):
        agent_code = mm_user.agent.agent_code
        return agent_code


class MobileMoneyRegistrationSerializer(serializers.ModelSerializer):
    agent_code = serializers.SerializerMethodField('get_agent_code')

    class Meta:
        model = MobileMoneyUsersRegistration
        fields = ['id', 'agent', 'agent_code', 'network', 'phone', 'name', 'id_type', 'id_number',
                  'date_registered', 'get_photo', 'photo']
        read_only_fields = ['agent']

    def get_agent_code(self, mm_user):
        agent_code = mm_user.agent.agent_code
        return agent_code


class MobileMoneyDepositSerializer(serializers.ModelSerializer):
    agent_code = serializers.SerializerMethodField('get_agent_code')

    class Meta:
        model = MobileMoneyDeposit
        fields = ['id', 'agent', 'agent_code', 'network', 'beneficiary_phone', 'beneficiary_name', 'depositor_phone',
                  'depositor_id_type', 'depositor_number', 'amount',
                  'date_deposited', ]
        read_only_fields = ['agent']

    def get_agent_code(self, mm_user):
        agent_code = mm_user.agent.agent_code
        return agent_code


class MobileMoneyWithDrawSerializer(serializers.ModelSerializer):
    agent_code = serializers.SerializerMethodField('get_agent_code')

    class Meta:
        model = MobileMoneyWithDraw
        fields = ['id', 'agent', 'agent_code', 'network', 'phone', 'amount', 'date_withdrew', ]
        read_only_fields = ['agent']

    def get_agent_code(self, mm_user):
        agent_code = mm_user.agent.agent_code
        return agent_code


class FraudSerializer(serializers.ModelSerializer):
    agent_code = serializers.SerializerMethodField('get_agent_code')
    agent_display_code = serializers.SerializerMethodField('get_agent_display_code')
    agent_phone = serializers.SerializerMethodField('get_agent_phone')

    class Meta:
        model = Fraud
        fields = ['id', 'agent', 'agent_code', 'agent_phone', 'agent_display_code', 'name', 'phone', 'reason',
                  'date_added']
        read_only_fields = ['agent']

    def get_agent_code(self, mm_user):
        agent_code = mm_user.agent.agent_code
        return agent_code

    def get_agent_display_code(self, mm_user):
        agent_display_code = mm_user.agent.agent_display_code
        return agent_display_code

    def get_agent_phone(self, mm_user):
        agent_phone = mm_user.agent.phone
        return agent_phone


class MomoPaySerializer(serializers.ModelSerializer):
    agent_code = serializers.SerializerMethodField('get_agent_code')

    class Meta:
        model = MomoPay
        fields = ['id', 'agent', 'agent_code', 'network', 'phone', 'amount', 'date_added']
        read_only_fields = ['agent']

    def get_agent_code(self, mm_user):
        agent_code = mm_user.agent.agent_code
        return agent_code


class AgentAccountsStartedSerializer(serializers.ModelSerializer):
    agent_code = serializers.SerializerMethodField('get_agent_code')

    class Meta:
        model = AgentsAccountsStartedWith
        fields = ['id', 'agent', 'agent_code', 'physical_cash', 'mtn_eCash', 'vodafone_eCash',
                  'airtel_tigo_eCash', 'ecobank_eCash',
                  'calbank_eCash', 'fidelity_eCash', 'ecash_sum', 'date_started']
        read_only_fields = ['agent']

    def get_agent_code(self, mm_user):
        agent_code = mm_user.agent.agent_code
        return agent_code


class AgentAccountsCompletedSerializer(serializers.ModelSerializer):
    agent_code = serializers.SerializerMethodField('get_agent_code')

    class Meta:
        model = AgentsAccountsCompletedWith
        fields = ['id', 'agent', 'agent_code', 'physical_cash', 'mtn_eCash', 'vodafone_eCash',
                  'airtel_tigo_eCash', 'ecobank_eCash',
                  'calbank_eCash', 'fidelity_eCash', 'ecash_sum', 'date_closed']
        read_only_fields = ['agent']

    def get_agent_code(self, mm_user):
        agent_code = mm_user.agent.agent_code
        return agent_code
