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
            'id', 'email', 'username', 'phone', 'company_name', 'full_name', 'region', 'regional_code',
            'agent_display_code')


class AuthenticatedPhoneAddressSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = AuthenticatedPhoneAddress
        fields = ['agent', 'username', 'phone_mac_address', 'authenticated_phone', 'date_added']
        read_only_fields = ['agent', 'authenticated_phone']

    def get_username(self, mm_user):
        username = mm_user.agent.username
        return username
