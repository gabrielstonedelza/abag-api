from djoser.serializers import UserCreateSerializer, UserSerializer
from rest_framework import serializers
from .models import User, AuthenticatedPhoneAddress


class UserCreateSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = User
        fields = ('id', 'email', 'username', 'password')


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id', 'email', 'agent_code', 'username', 'phone', 'company_name', 'full_name', 'region', 'regional_code',
            'agent_display_code')


class AuthenticatedPhoneAddressSerializer(serializers.ModelSerializer):
    agent_code = serializers.SerializerMethodField('get_agent_code')

    class Meta:
        model = AuthenticatedPhoneAddress
        fields = ['agent', 'agent_code', 'phone_mac_address', 'authenticated_phone', 'date_added']
        read_only_fields = ['agent', 'authenticated_phone']

    def get_agent_code(self, mm_user):
        agent_code = mm_user.agent.agent_code
        return agent_code
