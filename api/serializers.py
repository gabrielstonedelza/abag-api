from rest_framework import serializers
from .models import MobileMoneyUsersRegistration, MobileMoneyDeposit, MobileMoneyWithDraw


class MobileMoneyRegistrationSerializer(serializers.ModelSerializer):
    agent_code = serializers.SerializerMethodField('get_agent_code')

    class Meta:
        model = MobileMoneyUsersRegistration
        fields = ['id', 'agent', 'agent_code', 'network', 'phone', 'name', 'id_type', 'id_number',
                  'date_registered']
        read_only_fields = ['agent']

    def get_agent_code(self, mm_user):
        agent_code = mm_user.agent.agent_code
        return agent_code


class MobileMoneyDepositSerializer(serializers.ModelSerializer):
    agent_code = serializers.SerializerMethodField('get_agent_code')

    class Meta:
        model = MobileMoneyDeposit
        fields = ['id', 'agent', 'agent_code', 'network', 'phone', 'name', 'id_type', 'amount', 'date_deposited', ]
        read_only_fields = ['agent']

    def get_agent_code(self, mm_user):
        agent_code = mm_user.agent.agent_code
        return agent_code


class MobileMoneyWithDrawSerializer(serializers.ModelSerializer):
    agent_code = serializers.SerializerMethodField('get_agent_code')

    class Meta:
        model = MobileMoneyWithDraw
        fields = ['id', 'agent', 'agent_code', 'network', 'phone', 'name', 'id_type', 'amount', 'date_withdrew', ]
        read_only_fields = ['agent']

    def get_agent_code(self, mm_user):
        agent_code = mm_user.agent.agent_code
        return agent_code
