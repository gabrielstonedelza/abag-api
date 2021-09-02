from rest_framework import serializers
from .models import (MobileMoneyUsersRegistration, MobileMoneyDeposit, MobileMoneyWithDraw, AgencyBankingRegistration,
                     AgencyBankingDeposit, AgencyBankingWithDraw, Fraud, MomoPay)


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
        fields = ['id', 'agent', 'agent_code', 'bank', 'phone', 'other_phone', 'name', 'id_type', 'amount',
                  'date_deposited']
        read_only_fields = ['agent']

    def get_agent_code(self, agencydeposit):
        agent_code = agencydeposit.agent.agent_code
        return agent_code


class AgencyBankingWithDrawSerializer(serializers.ModelSerializer):
    agent_code = serializers.SerializerMethodField('get_agent_code')

    class Meta:
        model = AgencyBankingWithDraw
        fields = ['id', 'agent', 'agent_code', 'bank', 'phone', 'amount', 'date_withdrew']
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
        fields = ['id', 'agent', 'agent_code', 'network', 'phone', 'other_phone', 'name', 'id_type', 'amount',
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

    class Meta:
        model = Fraud
        fields = ['id', 'agent', 'agent_code', 'name', 'phone', 'reason', 'date_added']
        read_only_fields = ['agent']

    def get_agent_code(self, mm_user):
        agent_code = mm_user.agent.agent_code
        return agent_code


class MomoPaySerializer(serializers.ModelSerializer):
    agent_code = serializers.SerializerMethodField('get_agent_code')

    class Meta:
        model = MomoPay
        fields = ['id', 'agent', 'agent_code', 'network', 'phone', 'amount', 'date_added']
        read_only_fields = ['agent']

    def get_agent_code(self, mm_user):
        agent_code = mm_user.agent.agent_code
        return agent_code
